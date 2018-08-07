# Mission Not Impossible
# Author: Tran Quoc Thong
# email: thongqtran@outlook.com
# July 19 - August 7, Summer 2018

from sys import exit
from random import randint


class Scene(object):
    def enter_scene(self):
        print("This is just a parent class for 3 scenes: The Red Dragon Boat, the Night Market, The White Mansion")
        pass

class The_Red_Dragon_Boat (Scene):

    def enter_scene (self):
        print("\nYou enter the Red Dragon Boat..\n")
        password = input("Enter the correct password to unlock next scene\n> ")
        if password == '22444':
            return 'The Night Market'

class The_Night_Market (Scene):

    def enter_scene (self):
        print("\nYou enter the Night Market..\nCongratulation, you have finshed the first level of the game\nIn this level, you will need to find the leads you found from the boat, depends on what you found in the last level, you can pass this level with ease or with difficulty.....\nGAME STILL IN DEVELOPMENT....SORRY")
        exit(0)
        password = input("Enter the correct password to unlock next scene\n> ")
        if password == '22444':
            return 'The White Mansion'

class The_White_Mansion (Scene):

    def enter_scene (self):
        print("\nYou enter the White Mansion..\n")
        password = input("Enter the correct password to unlock next scene\n> ")
        if password == '22444':
            return 'Finish'

class Finish (Scene):

    def enter_scene(self):
        print("You've made it to the end! YOU WIN!")
        exit(1)


class maps(object):

    maps_dict ={
        'The Red Dragon Boat':The_Red_Dragon_Boat(),
        'The Night Market': The_Night_Market(),
        'The White Mansion': The_White_Mansion(),
        'Finish': Finish(),
    }

    def load_next_scene (self, scene_name):
        subclass_name = maps.maps_dict.get(scene_name)
        return subclass_name

    def start_playing (self):
        # IMPORTANT I am modifying the codes from ex45_innovation.py from using two classese to one class to control the changing of the level/scene
        #Update 1: TESTED OUTSIDE

        current_scene = self.load_next_scene('The Red Dragon Boat')
        last_level = self.load_next_scene('Finish')

        while current_scene != last_level:

            next_scene_name = current_scene.enter_scene()
            current_scene = self.load_next_scene(next_scene_name)

        current_scene.enter_scene()


#These 2 lines of codes are the start button of the game or the switching scene engine

"""start = maps()
start.start_playing()
"""



# This class allows users to explore rooms in the Red Dragon Boat
class Boat(object):

    def __init__(self):
        self.explored = False

    def enter_boat(self):
        pass

class control_room_boat (Boat):
    def enter_boat(self):
        print("\nJarvis: We're now in the Control Room.. \n")

        if randint(0, 1) and p.enemy.dead == False:
            p.enemy = Guard(c)
            stuff_12 = "%s encounters %s!" % (p.name, p.enemy.name)
            print(stuff_12)
            p.state = 'fight'
            p.enemy_attacks()
            gunControl.gun_control_fun()



            if self.explored == False:
              print("""There is no one in the room, let's see what's in here...
              You can:
              1) Enter the exact name of the item to take it (You can't remove the item once you choose)
              2) ['quit'] to exit the room
              """)
              itemList =['a Nano Ledger','a calendar with notes']
              number = 1
              for things in itemList:
                  print('[',number,'] '+ things)
                  number += 1
              take_item = 'dummy text'
              while take_item != 'quit' :
                  take_item = input("Take item> ")

                  if take_item not in i.getInventory() and take_item != 'quit' and take_item in itemList:
                      if len(i.getInventory()) <5:
                            i.addItem(take_item)
                            itemList.remove(take_item)
                            i.showInventory()
                            print("Items left: ",itemList)
                      else:
                            print("Your inventory is full! The limit is 5 items.")

              self.explored = True

        else:
          if self.explored == False:
              print("""There is no one in the room, let's see what's in here...
              You can:
              1) Enter the exact name of the item to take it (You can't remove the item once you choose)
              2) ['quit'] to exit the room
              """)
              itemList =['a Nano Ledger','a calendar with notes']
              number = 1
              for things in itemList:
                  print('[',number,'] '+ things)
                  number += 1
              take_item = 'dummy text'
              while take_item != 'quit':
                  take_item = input("Take item> ")
                  if take_item not in i.getInventory() and take_item != 'quit' and take_item in itemList:
                      if len(i.getInventory()) <5:
                            i.addItem(take_item)
                            itemList.remove(take_item)
                            i.showInventory()
                            print("Items left: ",itemList)
                      else:
                            print("Your inventory is full! The limit is 5 items.")
              self.explored =True
          else:
              print("\nJarvis: We have examine this room, nothing to check now..")


class main_lobby_boat (Boat):
    def enter_boat(self):
        print("\nJarvis: We're now in the Boat Lobby .. \n")

        if randint(0, 1) and p.enemy.dead == False:
            p.enemy = Guard(c)
            stuff_12 = "%s encounters %s!" % (p.name, p.enemy.name)
            print(stuff_12)
            p.state = 'fight'
            p.enemy_attacks()
            gunControl.gun_control_fun()

            if self.explored == False:
                print("""There is no one in the room, let's see what's in here...
                You can:
                1) Enter the exact name of the item to take it (You can't remove the item once you choose)
                2) ['quit'] to exit the room
                """)
                itemList =['a silver key','a Nokia phone']
                number = 1
                for things in itemList:
                    print('[',number,'] '+ things)
                    number += 1
                take_item = 'dummy text'
                while take_item != 'quit' :
                    take_item = input("Take item> ")

                    if take_item not in i.getInventory() and take_item != 'quit' and take_item in itemList:
                          if len(i.getInventory()) <5:
                                i.addItem(take_item)
                                itemList.remove(take_item)
                                i.showInventory()
                                print("Items left: ",itemList)
                          else:
                                print("Your inventory is full! The limit is 5 items.")
                self.explored = True


        else:
            if self.explored == False:
                print("""There is no one in the room, let's see what's in here...
                You can:
                1) Enter the exact name of the item to take it (You can't remove the item once you choose)
                2) ['quit'] to exit the room
                """)
                itemList =['a silver key','a Nokia phone']
                number = 1
                for things in itemList:
                    print('[',number,'] '+ things)
                    number += 1
                take_item = 'dummy text'
                while take_item != 'quit':
                    take_item = input("Take item> ")
                    if take_item not in i.getInventory() and take_item != 'quit' and take_item in itemList:
                        if len(i.getInventory()) <5:
                              i.addItem(take_item)
                              itemList.remove(take_item)
                              i.showInventory()
                              print("Items left: ",itemList)
                        else:
                              print("Your inventory is full! The limit is 5 items.")
                self.explored =True
            else:
                print("\nJarvis: We have examine this room, nothing to check now..")


class office_boat (Boat):
    def enter_boat(self):
        print("\nJarvis: We're now in the Office Room.. \n")

        if randint(0, 1) and p.enemy.dead == False:
            p.enemy = Guard(c)
            stuff_12 = "%s encounters %s!" % (p.name, p.enemy.name)
            print(stuff_12)
            p.state = 'fight'
            p.enemy_attacks()
            gunControl.gun_control_fun()

            if self.explored == False:
                print("""There is no one in the room, let's see what's in here...
                You can:
                1) Enter the exact name of the item to take it (You can't remove the item once you choose)
                2) ['quit'] to exit the room
                """)
                itemList =['a Dell laptop','a camera','a Xiaomi Red 5']
                number = 1
                for things in itemList:
                    print('[',number,'] '+ things)
                    number += 1
                take_item = 'dummy text'
                while take_item != 'quit' :
                    take_item = input("Take item> ")

                    if take_item not in i.getInventory() and take_item != 'quit' and take_item in itemList:
                          if len(i.getInventory()) <5:
                                i.addItem(take_item)
                                itemList.remove(take_item)
                                i.showInventory()
                                print("Items left: ",itemList)
                          else:
                                print("Your inventory is full! The limit is 5 items.")
                self.explored = True


        else:
            if self.explored == False:
                print("""There is no one in the room, let's see what's in here...
                You can:
                1) Enter the exact name of the item to take it (You can't remove the item once you choose)
                2) ['quit'] to exit the room
                """)
                itemList =['a Dell laptop','a camera','a Xiaomi Red 5']
                number = 1
                for things in itemList:
                    print('[',number,'] '+ things)
                    number += 1
                take_item = 'dummy text'
                while take_item != 'quit':
                    take_item = input("Take item> ")
                    if take_item not in i.getInventory() and take_item != 'quit' and take_item in itemList:
                        if len(i.getInventory()) <5:
                              i.addItem(take_item)
                              itemList.remove(take_item)
                              i.showInventory()
                              print("Items left: ",itemList)
                        else:
                              print("Your inventory is full! The limit is 5 items.")
                self.explored =True
            else:
                print("\nJarvis: We have examine this room, nothing to check now..")




class boat_nav (object):

    def __init__(self):
        pass

    def boat_room_navigate (self):

        switchControl = switch_control()

        boat_room_dict ={
            'control room': control_room_boat(),
            'main lobby room': main_lobby_boat(),
            'office room': office_boat(),
            'quit': 'quit',
        }

        print("""
        Boat Navigation Activated!

        You can go to ['control room']  or ['main lobby room'] or ['office room'] or ['quit']
        """)

        y = 1
        while y<1.0000000001:
            if p.state == 'fight':
                print("You are in a gun fight! Can't navigate room now!")
                break
            elif len(i.getInventory()) > 4:
                y +=2

            else:
                boat_room = input('Go to room> ')
                #map = self.boat_room_dict
                if boat_room in boat_room_dict.keys():

                    if boat_room == 'quit':
                        y += 2
                        print("Escape room navigation.")

                    else:
                        boat_room_dict[boat_room].enter_boat()
                else:
                    print("You can't go there\n",boat_room," is not on this boat.")



#These are the initiator for the control of the boat room changing control

"""
boat_room_control = boat_nav()
boat_room_control.boat_room_navigate()
"""

# This class is for player to explore rooms in the White Mansion
class Room (object):
    def __init__(self):
        pass


class Inventory(object):
    def __init__(self):
        self.inventory = []

    def addItem(self, item):
        #item = input("item to add: ")
        if len(self.inventory) < 5:
            self.inventory.append(item)
        else:
            print(f"\nYou are currently holding [{self.showInventory()}] items.\n You can't hold more than 5 items.\n")

    def removeItem(self,item):
        #item = input ("item to remove: ")
        if item in self.inventory:
            print("Removing item...", item)
            self.inventory.remove(item)
        else:
            print(item, "... not in your inventory.")

    def getInventory(self):
        InventoryList = []
        for item in self.inventory:
            InventoryList.append(item)
        return InventoryList

    def showInventory(self):
        if len(self.getInventory()) >0:
            print("You are currently have: ")
            i = 1
            for item in self.getInventory():
                print('['+ str(i)+ ']' + item)
                i+=1
        else:
            print("Your inventory is empty.  ¯\_(ツ)_/¯")


#Turns out I don't need the command system from James Gadoury at all
#But still need it as a parent class for other items (just because i don't feel like want to change those parent class for other items)
class Interactable(object):

    def __init__(self):
        pass
'''
    def interactWithObject(self):
        UI = input("Item Command> ")
        self.action = UI.rsplit(' ', 1)[0]

    def getUI(self):
        return self.action.lower()'''

#Research for Gun
#http://www.peimag.com/top-10-best-9mm-pistols-in-the-world/
#http://www.gunsandammo.com/reviews/glock-17-gen4-review/
#http://www.thetruthaboutguns.com/2012/10/foghorn/gun-review-glock-17/


# WORKING ON GUNS:
# Thinking about having different type of guns, have the silver watch as something to trade in the Night market
class Gun(Interactable):
    def __init__(self):
        Interactable.__init__(self)
        self.isUsable = True
        self.bulletCount = 3

    def getIsUsable (self):
        return self.isUsable

    def shootGun(self):
        self.bulletCount += -1
        if self.bulletCount ==0:
            self.isUsable = False
        return self.bulletCount

    def getBulletCount (self):
        return self.bulletCount


    #I don't know why would the player wants to throw the gun away, but I just put the option here

    def dropPistol (self):
        if 'gun' in i.getInventory():
            print("you drop the gun")
            i.removeItem('gun')
        else:
            print("You are not currently holding the gun!")


    def takePistol(self):
        if choose_gun == 'yes':
            if 'gun' not in i.getInventory():
                if self.getIsUsable() == True:
                    print("You pick up the gun")
                    print("It has two bullets in the clip and one in car's glove compactment.")
                    i.addItem('gun')
                    i.showInventory()
                else:
                    print("The gun is out of bullets. It is useless now.")
            else:
                print("You already have this gun on hand!")
        else:
            print("You DIDN'T RECIEVE the gun from the DRIVER!")

    def usePistol(self):
        #if 'gun' not in i.getInventory():
        #    print("You are not holding the gun!")
        if self.getIsUsable() == False:
            print("The gun is out of bullets. It is useless now.\nRemember you can ['reload'] for more bullets")
        else:
            self.shootGun()
            #r.engageRobot('attack robo')
            p.attack()



    def reloading (self):
        #if 'gun' not in i.getInventory():
        #    print("you are not holding the gun")
        #else:
        if 'gun' in i.getInventory():
            if p.state == 'fight':
                self.bulletCount += 1
                self.isUsable = True
                print("Remaining bullets: ", self.bulletCount)
                p.enemy_attacks()
                return self.bulletCount
            else:
                self.bulletCount += 1
                self.isUsable = True
                print("Remaining bullets: ", self.bulletCount)
                return self.bulletCount
        else:
            print ("You are not holding the gun!")

    def showBullet(self):
        if 'gun' in i.getInventory():
            print("Remaining bullets: ", self.bulletCount)
        else:
            print("You are not holding the gun!")

# the control system for the gun. Why can't I just control the gun from the player's control? Then I won't have to switchn control. Then no awkward control switching system.

# It's alright I will make the first version to be the awkward control switching system. The most crappy version of all.


class gun_control (object):


    g = Gun()
    gun_dict = {

    'take gun' : g.takePistol,
    'pick up gun':g.takePistol,
    'take the gun': g.takePistol,
    'pick up the gun':g.takePistol,

    'drop gun' :g.dropPistol,

    'shoot': g.usePistol,
    'shoot the guard': g.usePistol,
    'shoot guard': g.usePistol,
    'shoot gun':g.usePistol,

    'reload': g.reloading,

    'check bullets':g.showBullet,
    'check bullet':g.showBullet,
    'check gun':g.showBullet,
    'quit' : 'dummy text',
    }

    def gun_control_fun (self):
        if choose_gun == 'no':
            print("You didn't recieve the gun from the driver!")
            i.getInventory()
        else:
            print("""
            Gun Control Activated!

            You can do the following ['shoot'] or ['drop gun'] or ['pick up gun'] or ['reload'] or ['check bullet'] or ['quit']
            """)
            gunDict  = self.gun_dict
            x = 1 # Dam I was using i here and it's killing me with the error message:
            # UnboundLocalError: local variable 'i' referenced before assignment
            # and p.enemy.dead == False
            while x < 1.0001 and p.enemy.dead == False:
                command = input("Gun> ")
                if command in gunDict.keys():
                    if command == 'quit':
                        x += 1
                        print("Gun control deactivated.")
                    else:
                        gunDict[command]()
                else:
                    print("No gun command found!")


#More Items to play with here

class Umbrella(Interactable):
    def __init__(self):
        pass

class Keys(Interactable):
    def __init__(self):
        pass

class PuzzleItems(Interactable):
    def __init__ (self):
        pass

    def dell_laptop(self):
        if 'a Dell laptop' in i.getInventory():
            print("""
        You find a suspicious file says:

        Note for when all doors are locked: 123456

        Jarvis: This might be of help for your escape.
            """)
        else:
            print("This item is not in your inventory!")

    def camera (self):
        if 'a camera' in i.getInventory():
            print(f"""
        You find a picture of Mr. Anderson and a young dark hair woman.

        Jarvis: Great Job, {p.name}, now we have another lead.

        But I'm afraid this isn't going to help you escape.
        """)
        else:
            print("This item is not in your inventory!")

    def xiaomi_phone(self):
        if 'a Xiaomi Red 5' in i.getInventory():
            print("""
        二四百四六十万六百六

        You: What the heck is this?

        Jarvis: It is Chinese, we might also need to decode it to utf-8 if your WindowPowerShell can't read it. It seems like something can help us escape.
            """)
        else:
            print("This item is not in your inventory!")


    def sliver_key(self):
        if 'a silver key' in i.getInventory():
            print("""
        Jarvis: A Key? The door is locked by password. How could this help?
            """)
        else:
            print("This item is not in your inventory!")

    def nokia_phone(self):
        if 'a Nokia phone' in i.getInventory():
            print("""
        arvis: Wow, looks like there are some old contacts of Mr. Anderson. Wait a minute: Mr. Haadrikmaan? This is a great lead.
        """)
        else:
            print("This item is not in your inventory!")

    def nano_ledger(self):
        if 'a Nano Ledger' in i.getInventory():
            print("""
            Jarvis: What are we going to do with 99,999 FSN [Fusion] and 20.6 BTC [Bitcoin]?
            """)
        else:
            print("This item is not in your inventory!")


    def calendar(self):
        if 'a calendar with notes' in i.getInventory():
            print("""
        Jarvis: This seems to be Mr. Anderson's handwriting himself. What does it says here:

            [time] [number] like this 4 of 6 means ....

            What!!!! This part is teared off.
            """)
        else:
            print("This item is not in your inventory!")

    def gun_x (self):
        print("""
        This is your gun, there is no helpful information about it, quit wasting the time.
        """)

    def solve_puzzle (self):

        password = input("""
        Enter the correct password to unlock the Escape door\nPASSWORD>
        """)
        while password != 'quit':
            if password == '244466666':
                # IN THIS GAME VERSION 1.0 I AM NOT USING THE SCENE ENGINE that is used in the ZED A SHAW IN E.X43
                night.enter_scene()
            else:
                print ("WRONG PASSWORD!")

#All characters and players codes are below here

class Character(object):
    def __init__(self):
        #interactable.__init__(self)
        self.dead = False
        self.name = ""
        self.health = 1
        self.health_max = 1

    def killed(self):
        self.dead = True

    def isDead(self):
        return self.dead

    def defeat(self, enemy):
      #damage = randint(1,enemy.health)
      damage = min(  max(  randint(0, self.health) - randint(0, enemy.health),   0),  enemy.health )
      enemy.health = enemy.health - damage

      stuff_1 = "%s avoids %s's shot." % (enemy.name, self.name)
      stuff_2 = "%s hurts %s!" % (self.name, enemy.name)
      if damage == 0:
          print (stuff_1)
          print(f" {enemy.name}'s health status: {enemy.health}/{enemy.health_max}")
      else:
          print(stuff_2)
          print(f" {enemy.name}'s health status: {enemy.health}/{enemy.health_max}")
      return enemy.health <= 0

class Player(Character):

    def __init__(self):
        self.health = 100
        self.health_max = 100
        self.enemy = Guard(self)
        self.state = 'normal'

    def attack(self):

        if self.state == 'normal':
            g.shootGun()
            print("you are wasting bullet")
        elif self.state == 'fight':
            if self.defeat(self.enemy):
                stuff_17 = "%s kills %s!" % (self.name, self.enemy.name)
                print(stuff_17)
                print(f" {self.enemy.name}'s health status: {self.enemy.health}/{self.enemy.health_max}")
                self.enemy.killed()
                self.state = 'normal'
            else:
                self.enemy_attacks()


    def enemy_attacks(self):
      if self.enemy.defeat(self):
          stuff_19 = "%s was shot by %s!!!\nR.I.P." %(self.name, self.enemy.name)
          print(stuff_19)
          print(f" {self.name} health status: {self.health}/{self.health_max}")


class Guard (Character):

    def __init__(self, Guard):
        Character.__init__(self)
        self.name = 'a guard'
        self.health = randint(1, Guard.health)
        self.health_max = 50

    '''
    def engageGuard(self,UI):
        if self.isDead():
            print("The guard is already dead!")
        else:
            self.GuardsBattle()

    def GuardBattle(self):
        self.killed()
        print("The guards got shot! He is dead now.")
    '''

#More Characters:

class Man_In_Black (Character):
    def __init__(self):
        pass


class Mr_Anderson (Character):
    def __init__(self):
        pass


# Ballte Engine
#Battle engine is in Character class (and the gun class)


# Miscellaneous stuff (but important nontheless)
def error():
        print("*ERROR: You can't do that*")



# calling testing for battle:
'''
p.name = input ("Name: ")

g.engagePistol()
g.usePistol()
g.reloading()
g.showBullet()
'''





# Calling the classs for this
# Calling classes (must be after all of the classes being called)


g = Gun()
p = Player()
inter = Interactable()

c = Character()
i = Inventory()
gu = Guard(c)
boatNav= boat_nav()
gunControl = gun_control()
puzz = PuzzleItems()

night = The_Night_Market()





# Escalation in the game:

class boat_ending_scene(Scene):
        #boom_time = 1

    def examine_items(self):
        item_dict ={
        'dell laptop': puzz.dell_laptop,
        'camera': puzz.camera,
        'xiaomi phone': puzz.xiaomi_phone,
        'nokia phone': puzz.nokia_phone,
        'nano ledger': puzz.nano_ledger,
        'calendar': puzz.calendar,
        'gun':puzz.gun_x,
        'enter password':puzz.solve_puzzle,
        }

        command = input("\nWhen you figure out the password, type ['enter password']\nCheck item> ")
        if command in item_dict.keys():
            item_dict[command]()
        else:
            print("No command found!")

    def the_end(self):
        boom_time = 1
        while boom_time <10:


            if boom_time == 1:
                print("""

    BBBB UU ZZZZZZ !!!!!!!!!!!

    You: What's that Jarvis?

    Jarvis: From the Sattlite View, it seems like the other guards set the ship on a timing BOM. And they have locked you inside the boat. You need to find the way to escape.

    You: A BOMB? How? How do I escape?

    Jarvis: Look inside the files of the items you found. You will find a pass key for the escape door of the boat.

    Jarvis: You can't come back to those room now. And be quick before the boom goes off!
                """)

            print(i.showInventory())
            self.examine_items()


            if boom_time == 2:
                print("\n=== Find clue in your inventory to Unlock the escape door! ===\n")

            if boom_time == 5:
                print("Jarvis: QUICK! YOU DON't HAVE MUCH TIME! ")
            boom_time +=1

            if boom_time == 8:
                print( "THE BOOM IS ABOUT TO GOES OFF")

        print(" BOOOOOOOOOOMMMMMMMMMMMM !!!!! You are dead!")


boat_end = boat_ending_scene()





# Bulding the swtiching of console controls


class switch_control(object):


    def main_control (self):
        print( "\nMain Control: ")

        switch_dict = {
            'explore boat': boatNav.boat_room_navigate,
            'use gun': gunControl.gun_control_fun,
            'show items':i.showInventory,

        }

        print ("\nYou can do ['explore boat'] or ['use gun'] or ['show items']")

        while p.health > 0 and len(i.getInventory()) <5:
            command = input("Main Control> ")
            if command in switch_dict.keys():
                switch_dict[command]()
            else:
                print("No command found!")

        boat_end.the_end()



#Some instance has to be here to call for the classes:

switchControl = switch_control()

#GAME Starts below

p.name = input("\nAgent's name: ")




print(f"""
    WELCOME! You are playing: MISSION NOT IMPOSSIBLE - 2018

    Good Afternoon agent {p.name}:

    I am Jarvis, I will be your personal AI asisstant for this mission.

    Our driver  just arrived at this Red Dragon Boat, your mission is to investigate and find the leads to Mr. Anderson, the leader of the Red Heroin Trade.

    I will be with you the whole journey... but just as a voice... so be careful and take care of yourself!..
        """)

print("""
    Driver: "Son, here we're. Be careful."

    You: "Thanks."

    Driver: "Here is your weapon for the mission: A Glock 17 Gen 4th."
""")

choose_gun = input("Should you choose to accept the gun [yes] or [no]> ")
if choose_gun == 'yes':
    g.takePistol()
else:
    print("\nYou didn't take the gun... well best of luck!")


switchControl.main_control()


# Tran Quoc Thong
#thongqtran@outlook.com
#text_based_game: 
#beginner text based game in python
#July 24, 2018
#Finished: August 7, 2018
#Python 3.6.5
# Text game name: Mission Not Impossible
#Note on this game version 1.0
# to make this game I have sample lots of codes from James Gadoury and Francesco Balducci, and from Zed A Shaw too. Although I think that I modified them enough to be quit different from the original pieces.

# There are some still some imperfections to improve:
# 1- there are functions with are not necessary: like the choice for the gun, and the option to view show inventory (because without the other weapon choice - which will complicate the item part of the code, you don't need to choose the gun, and there is also nothing in the inventory to view - in the begining.)

# The game is quite linear (a linear story, not a dynamic story which can go in different directions), it forces the player to take the gun, to only have 1 enemy, which is super easy to kill - with 1 shot, to only pick 5 items and then the bomb goes off, the the player can't go back to the room and find another item.
 

#Technical limit of the game: the game doesn't let the player to drop the item he/she picks up and just let the player take the item randomly and can not change mind. And when the bomb starts, it's just luck that the player choose the right items to give clues to the player to guess the right password

#The intersting part is that the player can look into the clue from each item and figure out the lead for Mr. Anderson in next scene or to escape the boat and survive this round first.

# HOW TO PLAY?
#copy and paste the code in a text editor
#run it in a WindowPowershell like: python mission_not_impossible.py
