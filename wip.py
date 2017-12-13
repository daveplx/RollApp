import dicier

import kivy

kivy.require('1.10.0')

from kivy.core.window import Window
#Window.fullscreen = 'auto'
Window.borderless = True
#Window.clearcolor = (1, 1, 1, 0)

from kivy.app import App

from kivy.graphics import Rectangle

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class wipApp(App):

    def build(self):

        #root layout everything is placed in
        self.rootLayout = FloatLayout(size=Window.size)


        #layouts added on top of root

        #grid layout for dice and mod buttons
        self.buttonGrid = GridLayout(cols=5, rows=2, size_hint=(.95, .2), pos_hint={'x': .025, 'y': .7}, padding=10, spacing=5)
        self.rootLayout.add_widget(self.buttonGrid)

        #box layout for dice tray
        self.rollFrame = BoxLayout(size_hint=(.95, .2), pos_hint={'x': .025, 'y': .5}, padding=10, spacing=5)
        self.rootLayout.add_widget(self.rollFrame)

        #box layout for clear save roll buttons
        self.buttonBox = BoxLayout(size_hint=(.95, .1), pos_hint={'x': .025, 'y': .4}, padding=10, spacing=5)
        self.rootLayout.add_widget(self.buttonBox)

        #grid layout for results
        self.resultGrid = GridLayout(cols=1, rows=2, size_hint=(.95, .3), pos_hint={'x': .025, 'y': .1}, padding=10, spacing=5)
        self.rootLayout.add_widget(self.resultGrid)


        #buttons for the grid layout

        #self.buttonGrid.add_widget(Button(background_normal="img\\d4.png", size_hint=(.1, .2)))
        #d4
        self.button_d4 = Button(text='d4')
        self.button_d4.bind(on_press=self.scheduleRoll)
        self.buttonGrid.add_widget(self.button_d4)
        #d6
        self.button_d6 = Button(text='d6')
        self.button_d6.bind(on_press=self.scheduleRoll)
        self.buttonGrid.add_widget(self.button_d6)
        #d8
        self.button_d8 = Button(text='d8')
        self.button_d8.bind(on_press=self.scheduleRoll)
        self.buttonGrid.add_widget(self.button_d8)
        #d10
        self.button_d10 = Button(text='d10')
        self.button_d10.bind(on_press=self.scheduleRoll)
        self.buttonGrid.add_widget(self.button_d10)
        #d12
        self.button_d12 = Button(text='d12')
        self.button_d12.bind(on_press=self.scheduleRoll)
        self.buttonGrid.add_widget(self.button_d12)
        #d20
        self.button_d20 = Button(text='d20')
        self.button_d20.bind(on_press=self.scheduleRoll)
        self.buttonGrid.add_widget(self.button_d20)
        #d100
        self.button_d100 = Button(text='d100')
        self.button_d100.bind(on_press=self.scheduleRoll)
        self.buttonGrid.add_widget(self.button_d100)
        #dN
        self.button_dN = Button(text='dN')
        self.button_dN.bind(on_press=self.callback)
        self.buttonGrid.add_widget(self.button_dN)
        #mod
        self.button_mod = Button(text='Mod:')
        self.button_mod.bind(on_press=self.callback)
        self.buttonGrid.add_widget(self.button_mod)
        #modval
        self.button_modval = Button(text='+4')
        self.button_modval.bind(on_press=self.callback)
        self.buttonGrid.add_widget(self.button_modval)


        #roll frame and its button

        #roll frame
        self.diceTray = Button(size_hint=(.9, 1), text='omg so many dice.')
        self.rollFrame.add_widget(self.diceTray)
        #saved
        self.button_saved = Button(size_hint=(.1, 1), text='>')
        self.button_saved.bind(on_press=self.test)
        self.rollFrame.add_widget(self.button_saved)


        #button box and its buttons

        #clear
        self.button_clear = Button(text='clear')
        self.button_clear.bind(on_press=self.callback)
        self.buttonBox.add_widget(self.button_clear)
        #save
        self.button_save = Button(text='save')
        self.button_save.bind(on_press=self.callback)
        self.buttonBox.add_widget(self.button_save)

        #roll
        self.button_roll = Button(text='roll')
        self.button_roll.bind(on_press=self.roll)
        self.buttonBox.add_widget(self.button_roll)


        #result grid

        #dice
        self.dicerolls = Button(size_hint=(1, .7), pos_hint={'x': 0, 'y': .3}, text='I am dice.')
        self.resultGrid.add_widget(self.dicerolls)
        #total
        self.totalrolls = Button(size_hint=(1, .3), pos_hint={'x': 0, 'y': 0}, text='Total:')
        self.resultGrid.add_widget(self.totalrolls)


        #background
        with self.rootLayout.canvas.before:
            self.rect = Rectangle(size=self.rootLayout.size, source=("papyrus.jpg"))


        #return everything
        return self.rootLayout

    scheduledRolls = []

    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)

    def scheduleRoll(self, instance):
        self.scheduledRolls.append(instance.text)

    def clearRolls(self):
        self.scheduledRolls.clear()

    def sumList(self, list):
        sum = 0
        for num in list:
            sum += num
        return sum

    def condenseDiceList(self, list):
        condensedList = []
        for dice in list:
            contains = False
            splitDice = str(dice).split('d')
            for conDice in condensedList:
                splitConDice = str(conDice).split('d')
                if splitDice[1] == splitConDice[1]:
                    contains = True
                    conDice = str(int(splitConDice[0])+1) + 'd' + str(splitConDice[1])
            if not contains:
                condensedList.append(dice)
        return condensedList

    def roll(self, instance):
        scheduledDict = self.listToDict(self.scheduledRolls)
        for key in scheduledDict:
            rollString = str(scheduledDict[key])+key
            roll = dicier.roll(rollString)
            total = self.sumList(roll)
            print("%s -> %s (%s)" % (rollString, total, roll))
        self.clearRolls()


    def test(self, instance):
        pass

    def listToDict(self, list):
        dict = {}
        for die in list:
            if die in dict:
                dict[die] += 1
            else:
                dict[die] = 1
        return dict



if __name__ == '__main__':
    wipApp().run()