'''
Program: Screens.py
Author : Quang Hoang
Date   : 2019-10-07
Synopis: This contain all the screens and run them
'''

import os

def WelScr():
    print("")
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*				Enigma Machine                                 *")
    print("*                                                                              *")
    print("*                            For when you have                                 *")
    print("*                            something that needs                              *")
    print("*                            hiding or cracking!                               *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                    Programmers: CIS220 Class Fall 2019                       *")
    print("*                                                                              *")
    print("*                         Press any key to continue                            *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("********************************************************************************")
    sel = input("")
    return sel

def WelScrNext():
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	      Welcome! ")
    print("                             Encrpyt           1")
    print("                             Decrypt           2")
    print("                             Help              3")
    print("                             Program Settings  4")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Please make a selection.")

    if sel == "1":
        os.system("clear")
        WelScrNext()
    if sel == "2":
        os.system("clear")
        WelScrNext()
    if sel == "3":
        os.system("clear")
        helpScr()
    if sel == "4":
        os.system("clear")
        setting()
    else:
        os.system("clear")
        WelScrNext()

    return sel



def menu():
    print("")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	       Menu ")
    print("")
    print("				 Home		1")
    print("				 About		2")
    print("				 Encryption 	3")
    print("				 Decryption	4")
    print("				 Setting	5")
    print("				 Help		6")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to proceed: ")

    if sel == "1":
        os.system("clear")
        menu()
    if sel == "2":
        os.system("clear")
        menu()
    if sel == "3":
        os.system("clear")
        menu()
    if sel == "4":
        os.system("clear")
        menu()
    if sel == "5":
        os.system("clear")
        setting()
    if sel == "6":
        os.system("clear")
        helpScr()
    else:
        os.system("clear")
        menu()

    return sel

def setting():
    print("")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	      Setting ")
    print("")
    print("			    Change Rotor-1	    1")
    print("			    Change Rotor-2	    2")
    print("			    Change Rotor-3	    3")
    print("			    Change Plug Board	    4")
    print("			    Change Key		    5")
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to proceed: ")

    if sel == "1":
        os.system("clear")
        settingRotor_1()
    if sel == "2":
        os.system("clear")
        settingRotor_2()
    if sel == "3":
        os.system("clear")
        settingRotor_3()
    if sel == "4":
        os.system("clear")
        settingPlugBoard()
    if sel == "5":
        os.system("clear")
        settingKey()

    return sel

def settingRotor_1():
    print("")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	  Change Rotor-1")
    print("				")
    print("			    Rotor A		    1    ")
    print("			    Rotor B		    2")
    print("			    Rotor C		    3")
    print("			    Rotor D		    4")
    print("			    Rotor E		    5")
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to change rotor: ")
    return sel


def settingRotor_2():
    print("")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	  Change Rotor-2")
    print("				")
    print("			    Rotor A		    1    ")
    print("			    Rotor B		    2")
    print("			    Rotor C		    3")
    print("			    Rotor D		    4")
    print("			    Rotor E		    5")
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to change rotor: ")
    return sel

def settingRotor_3():
    print("")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	  Change Rotor-3")
    print("				")
    print("			    Rotor A		    1    ")
    print("			    Rotor B		    2")
    print("			    Rotor C		    3")
    print("			    Rotor D		    4")
    print("			    Rotor E		    5")
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to change rotor: ")
    return sel


def settingPlugBoard():
    print("")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	 Change Plug Board")
    print("				")
    print("		     To change your Plug Board please enter ")
    print("		     your new Plug Board name at the bottom. ")
    print("			    ")
    print("			- Thank You    ")
    print("			    ")
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Enter your new Plug Board name here: ")
    return sel

def settingKey():
    print("")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	    Change Key")
    print("				")
    print("		      ")
    sel = input("		    Enter Key:    ")
    print("			    ")
    print("			    ")
    print("			    ")
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    return sel


def helpScr():
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	      Help ")
    print("")
    print("			   Instructions		1")
    print("		           Info 		2")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Please enter a number.")

    if sel == "1":
        os.system("clear")
        instructions()
    if sel == "2":
        os.system("clear")
        helpScr()
    else:
        os.system("clear")
        helpScr()

    return sel


def instructions():
    print("")
    print("")
    print("")
    print("")
    print("				  Enigma Machine")
    print("")
    print("")
    print("			   	   Instruction ")
    print("")
    print("		Input text in the input box                       1	 ")
    print("		Press the button to encrypt text                  2	")
    print("		Wait for a second to get the encrypted text	  3")
    print("		press next button to encrypt other text           4	 ")
    print("		press clear button to clear the screen            5	 ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to proceed: ")

    return sel

## MAIN


os.system("clear")
WelScr()
os.system("clear")
WelScrNext()
