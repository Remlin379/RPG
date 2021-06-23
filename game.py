import sys
import random
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

items=[]
rooms=[]
enemies=[]

class item(object):
    def __init__(self,i,name,str,intl,agi,sta,attack,type,desc,hp,mana):
        self.id = i
        self.name = name
        self.str = str
        self.intl = intl
        self.agi = agi
        self.sta = sta
        self.attack = attack
        self.type = type
        self.description = desc
        self.hp = hp
        self.mana = mana

class expl(object):
    def __init__(self,nr,id,min,max,limit):
        self.nr=nr
        self.id=id
        self.minChance=min
        self.maxChance=max
        self.limit=limit

def init_items():
    global items
    items.append(item(0,"None",0,0,0,0,0,"","",0,0 ))
    items.append(item(1,"Admin sword",999,999,999,999,999,"weapon","slays enemies",0,0 ))
    items.append(item(2,"Admin helmet",999,999,999,999,999,"head","protects head",0,0))
    items.append(item(3,"Admin breastplate",999,999,999,999,999,"chest","protects chest",0,0 ))
    items.append(item(4,"Admin trousers",999,999,999,999,999,"legs","stylish",0,0 ))
    items.append(item(5,"Admin boots",999,999,999,999,999,"feet","tread carefully",0,0 ))
    items.append(item(6,"Apple",0,0,0,0,0,"consumable","A red fruit, tastes sweet",5,2))
    items.append(item(7,"Leather breastplate",0,0,0,5,0,"chest","A basic armor made out of leather",0,0))
    items.append(item(8,"Wooden sword",0,0,0,0,5,"weapon","A simple sword made out of wood",0,0))

class room(object):
    def __init__(self,i,a,b,N,E,S,W):
        self.id = i
        self.name = a
        self.text = b

        self.actions = {}
        self.explore = []
        self.stocks = {}

        self.north = N
        self.east = E
        self.south = S
        self.west = W

def init_rooms():
    global rooms
    rooms.append(room(0,"Starting area","A massive gate is right behind you. Pressumably, this is where you came from",1,-1,-1,-1))

    #rooms[0].actions.append("Explore")
    rooms[0].actions["Explore"]=0
    rooms[0].actions["Training dummy"]=2

    rooms[0].explore.extend((expl(0,-1,15,30,10),expl(1,-5,5,15,10),expl(2,-10,1,5,5),expl(3,6,30,50,6)))

    rooms.append(room(1,"Plaza","As you come down from massive stairs, you see a lot of people gathered, most of them being merchants offering their wares to other people",2,13,0,14))

    rooms[1].actions["Weapons"] = 1
    rooms[1].actions["Armor"] = 1
    rooms[1].actions["Consumables"] = 1
    rooms[1].stocks["Consumables"] = {"Apple":(6,4)}
    rooms[1].stocks["Armor"] = {"Leather breastplate": (7,50)}
    rooms[1].stocks["Weapons"] = {"Wooden sword": (8,25)}


    rooms.append(room(2,"City block 1","City block 1",3,-1,1,-1))

    rooms.append(room(3,"City block 2","City block 2",4,5,2,22))

    rooms.append(room(4,"City block 3","City block 3",23,6,3,21))

    rooms.append(room(5,"City block 4","City block 4",6,-1,-1,3))

    rooms.append(room(6,"City block 5","City block 5",-1,7,5,4))

    rooms.append(room(7,"City block 6","City block 6",-1,8,-1,6))

    rooms.append(room(8,"City block 7","City block 7",-1,-1,9,7))

    rooms.append(room(9,"City block 8","City block 8",8,-1,10,-1))

    rooms.append(room(10,"City block 9","City block 9",9,-1,11,-1))

    rooms.append(room(11,"City block 10","City block 10",10,-1,-1,12))

    rooms.append(room(12,"City block 11","City block 11",-1,11,-1,13))

    rooms.append(room(13,"City block 12","City block 12",-1,12,-1,1))

    rooms.append(room(14,"City block 13","City block 13",-1,1,-1,15))

    rooms.append(room(15,"City block 14","City block 14",-1,14,-1,16))

    rooms.append(room(16,"City block 15","City block 15",17,15,-1,-1))

    rooms.append(room(17,"City block 16","City block 16",18,-1,16,-1))

    rooms.append(room(18,"City block 17","City block 17",19,-1,17,-1))

    rooms.append(room(19,"City block 18","City block 18",-1,20,18,-1))

    rooms.append(room(20,"City block 19","City block 19",-1,21,-1,19))

    rooms.append(room(21,"City block 20","City block 20",-1,4,22,20))

    rooms.append(room(22,"City block 21","City block 21",21,3,-1,-1))

    rooms.append(room(23,"Gate","You can see a big gate here, this is the only entrance to the city. ",-1,-1,4,-1))



class character(object):
    def __init__(self):
        self.level = 1
        self.gold = 0
        self.points = 5
        self.strength = 5
        self.intelligence = 5
        self.agility = 5
        self.stamina = 5
        self.luck = 5
        self.experience = 0
        self.maxHealth = self.stamina*2+self.level
        self.currentHealth = self.maxHealth

        self.inventory = []
        self.head = 0
        self.chest = 0
        self.legs = 0
        self.feet = 0
        self.weapon = 0

class npc(object):
    def __init__(self,i,name,lvl,gold,str,int,agi,sta,luc):
        self.id = i
        self.name = name
        self.level = lvl
        self.gold = gold
        self.strength = str
        self.intelligence = int
        self.agility = agi
        self.stamina = sta
        self.luck = luc
        self.experience = 0
        self.maxHealth = self.stamina*2+self.level
        self.currentHealth = self.maxHealth

        self.dialog=[]
        self.answer=[]

        self.special=0

        #self.combat

def init_enemy():
        enemies.append(npc(0,"Training dummy",0,0,10,0,0,999999,0))



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("main.ui", self)

        init_items()
        init_rooms()
        init_enemy()
        self.inCombat = 0


        #variable init

        self.fontSettings = ""
        self.mc=character()

        self.currentLocation = 0


        #test
        self.mc.inventory.append(1)
        self.mc.inventory.append(2)
        self.mc.inventory.append(3)
        self.mc.inventory.append(4)
        self.mc.inventory.append(5)
        self.mc.inventory.append(4)
        self.mc.inventory.append(3)
        self.mc.inventory.append(2)
        self.mc.inventory.append(1)
        self.mc.inventory.append(5)


        #Widget init
        self.log = self.findChild(QtWidgets.QListWidget,'gameLog')
        self.clock = self.findChild(QtWidgets.QTimeEdit,'timeEdit')

        self.mainPage = self.findChild(QtWidgets.QStackedWidget,"Main")
        self.restart = self.findChild(QtWidgets.QAction,"actionRestart")
        self.newGame = self.findChild(QtWidgets.QPushButton,"newGame")


        self.restart.triggered.connect(self.restart_)
        self.newGame.clicked.connect(self.new_game)

        self.tabActions = self.findChild(QtWidgets.QTabWidget,'actions')
        self.tabData = self.findChild(QtWidgets.QTabWidget,'Data')

        self.mainText = self.findChild(QtWidgets.QPlainTextEdit,'MainText')
        self.mainText.setPlainText(rooms[0].text)

        #combat gui
        self.combatPage = self.findChild(QtWidgets.QStackedWidget,"combatSwap")
        self.health = self.findChild(QtWidgets.QProgressBar,'health')

        self.enemyName = self.findChild(QtWidgets.QLabel,'enemyName')
        self.enemyHealth = self.findChild(QtWidgets.QProgressBar,'enemyHealth')

            #level buttons
        self.strUp = self.findChild(QtWidgets.QPushButton,'strUp')
        self.intUp = self.findChild(QtWidgets.QPushButton, 'intUp')
        self.agiUp = self.findChild(QtWidgets.QPushButton, 'agiUp')
        self.staUp = self.findChild(QtWidgets.QPushButton, 'staUp')
        self.lucUp = self.findChild(QtWidgets.QPushButton, 'lucUp')
        self.levelUp = self.findChild(QtWidgets.QPushButton, 'levelUp')


        self.levelUp.hide()

        self.strUp.clicked.connect(lambda: self.stats_add(1))
        self.intUp.clicked.connect(lambda: self.stats_add(2))
        self.agiUp.clicked.connect(lambda: self.stats_add(3))
        self.staUp.clicked.connect(lambda: self.stats_add(4))
        self.lucUp.clicked.connect(lambda: self.stats_add(5))





            #Stats
        self.points = self.findChild(QtWidgets.QLineEdit, 'pointsShow')
        self.str = self.findChild(QtWidgets.QLineEdit,'strShow')
        self.intl = self.findChild(QtWidgets.QLineEdit, 'intShow')
        self.agi = self.findChild(QtWidgets.QLineEdit, 'agiShow')
        self.sta = self.findChild(QtWidgets.QLineEdit, 'staShow')
        self.luc = self.findChild(QtWidgets.QLineEdit, 'lucShow')
        self.money = self.findChild(QtWidgets.QLineEdit,'goldShow')

        self.points.setText(str(self.mc.points))
        self.str.setText(str(self.mc.strength))
        self.intl.setText(str(self.mc.intelligence))
        self.agi.setText(str(self.mc.agility))
        self.sta.setText(str(self.mc.stamina))
        self.luc.setText(str(self.mc.luck))
        self.money.setText(str(self.mc.gold))


            #settings
        self.darkMode = self.findChild(QtWidgets.QAction,'actionDark_mode')

        self.fontSmall = self.findChild(QtWidgets.QAction,'actionSmall')
        self.fontMedium = self.findChild(QtWidgets.QAction, 'actionMedium')
        self.fontBig = self.findChild(QtWidgets.QAction, 'actionBig')
        self.fontCustom = self.findChild(QtWidgets.QAction,'actionCustom')

        self.fontSmall.triggered.connect(self.font_size)
        self.fontMedium.triggered.connect(self.font_size)
        self.fontBig.triggered.connect(self.font_size)
        self.fontCustom.triggered.connect(self.font_custom)

        self.darkMode.triggered.connect(self.dark_mode)

            #inventory
        self.inventory = self.findChild(QtWidgets.QListWidget,'listInventory')
        self.itemDesc = self.findChild(QtWidgets.QPlainTextEdit,'itemDescription')

        self.head = self.findChild(QtWidgets.QComboBox,'headBox')
        self.chest = self.findChild(QtWidgets.QComboBox,'chestBox')
        self.legs = self.findChild(QtWidgets.QComboBox,'legsBox')
        self.feet = self.findChild(QtWidgets.QComboBox,'feetBox')
        self.weapon = self.findChild(QtWidgets.QComboBox,'weaponBox')

        self.prevHead=0
        self.prevChest=0
        self.prevLegs=0
        self.prevFeet=0
        self.prevWeapon=0

        for i in self.mc.inventory:
            self.inventory.addItem(items[i].name)

        self.inventory.currentItemChanged.connect(self.item_desc)

        for i in self.mc.inventory:
            if items[i].type == "head":
               self.head.addItem(items[i].name)
            elif items[i].type == "chest":
               self.chest.addItem(items[i].name)
            elif items[i].type == "legs":
               self.legs.addItem(items[i].name)
            elif items[i].type == "feet":
               self.feet.addItem(items[i].name)
            elif items[i].type == "weapon":
               self.weapon.addItem(items[i].name)



        self.head.currentTextChanged.connect(self.equip)
        self.chest.currentTextChanged.connect(self.equip)
        self.legs.currentTextChanged.connect(self.equip)
        self.feet.currentTextChanged.connect(self.equip)
        self.weapon.currentTextChanged.connect(self.equip)


        #Navigation
        self.moveNorth = self.findChild(QtWidgets.QPushButton,'navNorth')
        self.moveEast = self.findChild(QtWidgets.QPushButton, 'navEast')
        self.moveSouth = self.findChild(QtWidgets.QPushButton, 'navSouth')
        self.moveWest = self.findChild(QtWidgets.QPushButton, 'navWest')


        self.moveEast.setEnabled(False)
        self.moveSouth.setEnabled(False)
        self.moveWest.setEnabled(False)


        self.moveNorth.clicked.connect(self.moveTo)
        self.moveEast.clicked.connect(self.moveTo)
        self.moveSouth.clicked.connect(self.moveTo)
        self.moveWest.clicked.connect(self.moveTo)

        self.actionButtons = []
        q=1
        while q<=40:
            self.actionButtons.append(self.findChild(QtWidgets.QPushButton,'a'+str(q)))
            self.actionButtons[q-1].clicked.connect(self.doAction)
            q+=1

        q=0

        for key in rooms[self.currentLocation].actions:
            self.actionButtons[q].setText(key)
            self.actionButtons[q].setEnabled(True)
            q+=1



        #test
        self.miniMap = []

        q=0
        while q<49:
            self.miniMap.append(self.findChild(QtWidgets.QPushButton,'m'+str(q)))
            q+=1


        self.mapMatrix = []

        q=0
        while q<=20:
            self.mapMatrix.append([])
            q+=1

        q=0
        w=0
        while q<=20:
            w=0
            while w<=20:
                self.mapMatrix[q].append(-1)
                w+=1
            q+=1
        self.to_matrix(0,10,10)

        self.generate_minimap()
        #Widget actions




    def to_matrix(self,room,x,y):
        self.mapMatrix[x][y]=room

        if rooms[room].north!=-1 and self.mapMatrix[x-1][y]==-1:
            self.to_matrix(rooms[room].north,x-1,y)
        if rooms[room].south!=-1 and self.mapMatrix[x+1][y]==-1:
            self.to_matrix(rooms[room].south,x+1,y)
        if rooms[room].east!=-1 and self.mapMatrix[x][y+1]==-1:
            self.to_matrix(rooms[room].east,x,y+1)
        if rooms[room].west!=-1 and self.mapMatrix[x][y-1]==-1:
            self.to_matrix(rooms[room].west,x,y-1)
    #Widget functions


    def font_size(self):
        siz=self.sender()
        if siz.text()=="Small":
            font = QFont("Verdana", 8)
        elif siz.text()=="Medium":
            font = QFont("Verdana", 12)
        elif siz.text()=="Big":
            font = QFont("Verdana", 20)
        self.mainText.setFont(font)

    def font_custom(self):
        dlg,ok=QFontDialog.getFont()
        if ok:
            self.mainText.setFont(dlg)
            self.fontSettings=dlg

    def dark_mode(self):
        if self.darkMode.isChecked():
            self.setStyleSheet("background-color: #1b1c1c; color: white; }; ")
            self.tabActions.setStyleSheet("QTabWidget::pane { border: 0;} QTabBar::tab{color:black; width: 200%;};")
            self.tabData.setStyleSheet("QTabWidget::pane { border: 0;} QTabBar::tab{color:black;}")
        else:
            self.setStyleSheet("QTabWidget::pane { border: 0;}")
            self.tabActions.setStyleSheet("QTabBar::tab { width: 200%; }")

    def stats_add(self,stat):
        if stat==1:
            self.mc.strength+=1
            self.str.setText(str(self.mc.strength))
        elif stat==2:
            self.mc.intelligence+=1
            self.intl.setText(str(self.mc.intelligence))
        elif stat==3:
            self.mc.agility+=1
            self.agi.setText(str(self.mc.agility))
        elif stat==4:
            self.mc.stamina+=1
            self.sta.setText(str(self.mc.stamina))
        elif stat==5:
            self.mc.luck+=1
            self.luc.setText(str(self.mc.luck))

        self.mc.points -= 1
        self.points.setText(str(self.mc.points))
        if self.mc.points==0:
            self.strUp.hide()
            self.intUp.hide()
            self.agiUp.hide()
            self.staUp.hide()
            self.lucUp.hide()

    def item_desc(self):
        for i in items:
            if i.name == self.inventory.currentItem().text():
                self.itemDesc.setPlainText(i.description+"\nstr: "+str(i.str)+"\nint: "+str(i.intl)+"\nagi: "+str(i.agi)+"\nst: "+str(i.sta))
                break

    def equip_sub(self,i):
        self.mc.strength -= items[i].str
        self.mc.intelligence -= items[i].intl
        self.mc.agility -= items[i].agi
        self.mc.stamina -= items[i].sta

    def equip_add(self,i):
        self.mc.strength += items[i].str
        self.mc.intelligence += items[i].intl
        self.mc.agility += items[i].agi
        self.mc.stamina += items[i].sta

    def equip(self):
        x=self.sender().currentText()
        for i in items:
            if i.name == x:
                if i.type=="head":
                    self.mc.head=i.id
                    self.equip_sub(self.prevHead)
                    self.equip_add(i.id)
                    self.prevHead=i.id
                elif i.type=="chest":
                    self.mc.chest=i.id
                    self.equip_sub( self.prevChest)
                    self.equip_add(i.id)
                    self.prevChest=i.id
                elif i.type=="legs":
                    self.mc.legs=i.id
                    self.equip_sub(self.prevLegs)
                    self.equip_add(i.id)
                    self.prevLegs = i.id
                elif i.type=="feet":
                    self.mc.feet=i.id
                    self.equip_sub(self.prevFeet)
                    self.equip_add(i.id)
                    self.prevFeet = i.id
                elif i.type=="weapon":
                    self.mc.weapon=i.id
                    self.equip_sub(self.prevWeapon)
                    self.equip_add(i.id)
                    self.prevWeapon = i.id
                else:
                    if self.head.currentText() == "None":
                        self.mc.head = 0
                        self.equip_sub(self.prevHead)
                        self.prevHead = i.id
                    if self.chest.currentText() == "None":
                        self.mc.chest = 0
                        self.equip_sub(self.prevChest)
                        self.prevChest = i.id
                    if self.legs.currentText() == "None":
                        self.mc.legs = 0
                        self.equip_sub(self.prevLegs)
                        self.prevLegs = i.id
                    if self.feet.currentText() == "None":
                        self.mc.feet = 0
                        self.equip_sub(self.prevFeet)
                        self.prevFeet = i.id
                    if self.weapon.currentText() == "None":
                        self.mc.weapon = 0
                        self.equip_sub(self.prevWeapon)
                        self.prevWeapon = i.id
                self.str.setText(str(self.mc.strength))
                self.intl.setText(str(self.mc.intelligence))
                self.agi.setText(str(self.mc.agility))
                self.sta.setText(str(self.mc.stamina))
                break



    def generate_minimap(self):
        for i in self.miniMap:
            i.setStyleSheet("border:none; background-color:white;")
            i.setText("")
        y=0
        c=0

        for i in self.mapMatrix:
            x=0
            for j in i:
                if j==self.currentLocation:
                    c=1
                    break
                x+=1
            if c==1:
                break
            y+=1

        startX=x-3
        endX=x+4
        temp = startX

        startY=y-3
        endY=y+4


        q=0
        while startY<endY:
            startX=temp
            while startX<endX:
                if self.mapMatrix[startY][startX]!=-1:
                    self.miniMap[q].setStyleSheet("border:1px solid gray; background-color:yellow;")
                q+=1
                startX+=1


            startY+=1
        self.miniMap[24].setStyleSheet("border:1px solid gray; background-color:red;")



    def moveTo(self):
        direction = self.sender()

        if direction.text() == "N":
            self.currentLocation=rooms[self.currentLocation].north
            self.log.insertItem(0,"Moved North")
        elif direction.text() == "E":
            self.currentLocation=rooms[self.currentLocation].east
            self.log.insertItem(0,"Moved East")
        elif direction.text() == "S":
            self.currentLocation=rooms[self.currentLocation].south
            self.log.insertItem(0,"Moved South")
        elif direction.text() == "W":
            self.currentLocation=rooms[self.currentLocation].west
            self.log.insertItem(0,"Moved West")

        self.mainText.setPlainText(rooms[self.currentLocation].text)

        if rooms[self.currentLocation].north != -1:
            self.moveNorth.setEnabled(True)
        elif rooms[self.currentLocation].north == -1:
            self.moveNorth.setEnabled(False)

        if rooms[self.currentLocation].east != -1:
            self.moveEast.setEnabled(True)
        elif rooms[self.currentLocation].east == -1:
            self.moveEast.setEnabled(False)

        if rooms[self.currentLocation].south != -1:
            self.moveSouth.setEnabled(True)
        elif rooms[self.currentLocation].south == -1:
            self.moveSouth.setEnabled(False)

        if rooms[self.currentLocation].west != -1:
            self.moveWest.setEnabled(True)
        elif rooms[self.currentLocation].west == -1:
            self.moveWest.setEnabled(False)
        q=0
        #while q<40:
        #    try:
        #        self.actionButtons[q].setText(str(rooms[self.currentLocation].actions[q]))
        #        self.actionButtons[q].setEnabled(True)
        #    except:
        #        self.actionButtons[q].setText("")
        #        self.actionButtons[q].setEnabled(False)
        #    q+=1

        self.generate_minimap()

        for key in rooms[self.currentLocation].actions:
            self.actionButtons[q].setText(key)
            self.actionButtons[q].setEnabled(True)
            self.actionButtons[q].setToolTip("")
            q+=1
        while q<40:
            self.actionButtons[q].setText("")
            self.actionButtons[q].setEnabled(False)
            self.actionButtons[q].setToolTip("")
            q+=1



    def explore(self):


        x=randint(0,100)
        q=0
        for i in rooms[self.currentLocation].explore:
            if x>=i.minChance and x<i.maxChance:
                if i.id>=0:
                    if i.limit>0:
                        self.mc.inventory.append(i.id)
                        self.inventory.addItem(items[i.id].name)
                        self.log.insertItem(0, "Found "+items[i.id].name.lower())
                        rooms[self.currentLocation].explore[i.nr].limit-=1
                        self.mainText.setPlainText(rooms[self.currentLocation].text+"\n\n\n"+"Found "+items[i.id].name.lower())
                        q = 1

                else:
                    if rooms[self.currentLocation].explore[i.nr].limit>0:
                        self.mc.gold+=abs(i.id)
                        self.money.setText(str(self.mc.gold))
                        self.log.insertItem(0, "Found " + str(abs(i.id))+" gold")
                        self.mainText.setPlainText(rooms[self.currentLocation].text + "\n\n\n" + "Found " + str(abs(i.id))+" gold")
                        rooms[self.currentLocation].explore[i.nr].limit -= 1
                        q = 1

        if q==0:
            self.mainText.setPlainText(rooms[self.currentLocation].text+"\n\n\n"+"Found nothing")
            self.log.insertItem(0, "Found nothing")



    def buy(self,item):
        price=rooms[self.currentLocation].stocks[self.currentShop][item][1]
        for i in items:
            if i.name==item:
                self.mc.inventory.append(i.id)
                break
        self.inventory.addItem(item)
        self.mc.gold-=price
        self.money.setText(str(self.mc.gold))
        self.log.insertItem(0,"Bought "+item)
        if self.mc.gold<price:
            self.open_shop(self.currentShop)

    def open_shop(self,shop):
        q=0
        for key in rooms[self.currentLocation].stocks[shop]:
            self.actionButtons[q].setText(key)
            if rooms[self.currentLocation].stocks[shop][key][1]<=self.mc.gold:
                #print(rooms[self.currentLocation].stocks[shop][key][1], self.mc.gold)
                self.actionButtons[q].setEnabled(True)
            else:
                self.actionButtons[q].setEnabled(False)
                self.actionButtons[q].setToolTip("Not enough gold")
            q+=1
        while q<40:
            self.actionButtons[q].setText("")
            self.actionButtons[q].setEnabled(False)
            q+=1

        self.currentShop=shop

        self.actionButtons[19].setText("Back")
        self.actionButtons[19].setEnabled(True)
        self.actionButtons[39].setText("Back")
        self.actionButtons[39].setEnabled(True)


    def enemy_action(self,*args):

        z=0

        rand=randint(-200,200)/1000
        rand+=1
        for x in args:
            if x=="defend":
                dmg = (rand * self.currentEnemy.strength)/2
                z=1
        if z==0:
            dmg=rand*self.currentEnemy.strength
        self.mc.currentHealth -= dmg
        hp = int(self.mc.currentHealth / self.mc.maxHealth * 100)
        if hp<0:
            hp=0
        self.mainText.appendPlainText("You got hit for "+str(int(dmg))+" damage")
        print(hp)
        self.health.setValue(hp)



    def combat(self,action):
        print(action)

        if action=="Run":
            if self.currentEnemy.special==1:
                self.mainText.appendText("\n\n\nEscape failed")
                self.enemy_action()
            else:
                chance = (self.mc.level - self.currentEnemy.level+5)*10
                if randint(0,50)<chance:
                    self.mainText.setPlainText(rooms[self.currentLocation].text+"\n\n\nEscaped sucessfully")
                    self.inCombat=False
                    self.combatPage.setCurrentIndex(0)
                    self.set_room()
                else:
                    self.mainText.appendPlainText("\n\n\nEscape failed")
                    self.enemy_action()
        elif action=="Attack":
            if self.mc.weapon==0:
                self.currentEnemy.currentHealth-=self.mc.strength
                dmg=self.mc.strength
            else:
                rand=randint(-200,200)/1000
                rand+=1
                print(rand)
                self.currentEnemy.currentHealth-=rand*(items[self.mc.weapon].attack*(1+(self.mc.strength/10)))
                dmg = rand*(items[self.mc.weapon].attack*(1+(self.mc.strength/10)))

            hp=int(self.currentEnemy.currentHealth/self.currentEnemy.maxHealth*100)
            if hp<0:
                hp=0
            self.mainText.appendPlainText("\nYou dealt "+str(int(dmg))+" damage")
            self.enemyHealth.setValue(hp)
            self.enemy_action()
        elif action=="Defend":
            self.enemy_action("defend")



    def open_combat(self):
        self.inCombat = True
        self.combatPage.setCurrentIndex(1)
        self.currentEnemy= enemies[0]##########
        self.enemyName.setText(self.currentEnemy.name)
        self.enemyHealth.setValue(100)

        self.moveWest.setEnabled(False)
        self.moveSouth.setEnabled(False)
        self.moveNorth.setEnabled(False)
        self.moveEast.setEnabled(False)
        self.clear_buttons()

        self.actionButtons[0].setText("Attack")
        self.actionButtons[0].setEnabled(True)

        self.actionButtons[1].setText("Skills")
        self.actionButtons[1].setEnabled(True)

        self.actionButtons[3].setText("Run")
        self.actionButtons[3].setEnabled(True)

        self.actionButtons[4].setText("Defend")
        self.actionButtons[4].setEnabled(True)

        self.actionButtons[5].setText("Items")
        self.actionButtons[5].setEnabled(True)

        self.actionButtons[7].setText("Surrender")
        self.actionButtons[7].setEnabled(True)

    def doAction(self,*args):
        if self.inCombat:
            self.combat(self.sender().text())
        else:
            try:
                if rooms[self.currentLocation].actions[self.sender().text()]==0:
                    self.explore()
                elif rooms[self.currentLocation].actions[self.sender().text()]==1:
                    self.open_shop(self.sender().text())
                elif rooms[self.currentLocation].actions[self.sender().text()]==2:
                    self.open_combat()

                #elif coś daje combat:

            except:
                if self.sender().text()=="Back":
                    self.set_room()
                else:
                    self.buy(self.sender().text())

    def reset_action(self):
        q=1
        while q<=40:
            self.actionButtons[q-1].disconnect()
            self.actionButtons[q-1].clicked.connect(self.doAction)
            q+=1

    def set_room(self):
        q = 0
        for key in rooms[self.currentLocation].actions:
            self.actionButtons[q].setText(key)
            self.actionButtons[q].setEnabled(True)
            self.actionButtons[q].setToolTip("")
            q += 1
        while q < 40:
            self.actionButtons[q].setText("")
            self.actionButtons[q].setEnabled(False)
            self.actionButtons[q].setToolTip("")
            q += 1

        if rooms[self.currentLocation].north != -1:
            self.moveNorth.setEnabled(True)
        elif rooms[self.currentLocation].north == -1:
            self.moveNorth.setEnabled(False)

        if rooms[self.currentLocation].east != -1:
            self.moveEast.setEnabled(True)
        elif rooms[self.currentLocation].east == -1:
            self.moveEast.setEnabled(False)

        if rooms[self.currentLocation].south != -1:
            self.moveSouth.setEnabled(True)
        elif rooms[self.currentLocation].south == -1:
            self.moveSouth.setEnabled(False)

        if rooms[self.currentLocation].west != -1:
            self.moveWest.setEnabled(True)
        elif rooms[self.currentLocation].west == -1:
            self.moveWest.setEnabled(False)


    def clear_buttons(self):
        q=0
        while q<40:
            self.actionButtons[q].setText("")
            self.actionButtons[q].setEnabled(False)
            self.actionButtons[q].setToolTip("")
            q+=1
    def restart_(self):
        self.mainPage.setCurrentIndex(1)
    def new_game(self):
        self.mainPage.setCurrentIndex(0)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()