"""
RYM album chooser two
More efficient version with functions

"""
import random, webbrowser, colorama
from termcolor import colored, cprint

colorama.init()

def showPurpose():
    print("\t=================================================================================================")
    cprint("""\n\t█▄▄▄▄ ▀▄    ▄ █▀▄▀█     ██   █     ███     ▄   █▀▄▀█     █ ▄▄  ▄█ ▄█▄    █  █▀ ▄███▄   █▄▄▄▄
\t█  ▄▀   █  █  █ █ █     █ █  █     █  █     █  █ █ █     █   █ ██ █▀ ▀▄  █▄█   █▀   ▀  █  ▄▀
\t█▀▀▌     ▀█   █ ▄ █     █▄▄█ █     █ ▀ ▄ █   █ █ ▄ █     █▀▀▀  ██ █   ▀  █▀▄   ██▄▄    █▀▀▌
\t█  █     █    █   █     █  █ ███▄  █  ▄▀ █   █ █   █     █     ▐█ █▄  ▄▀ █  █  █▄   ▄▀ █  █
\t  █    ▄▀        █         █     ▀ ███   █▄ ▄█    █       █     ▐ ▀███▀    █   ▀███▀     █
\t ▀              ▀         █               ▀▀▀    ▀         ▀              ▀             ▀
                         ▀                                                                   """, "cyan")
    print("\t=================================================================================================")
    cprint("""\tPurpose: Given your RateYourMusic account name and
    \tanmount of pages with unlisted albums, will randomly pick a page and an album
    \tfor you to listen to.\n""", "cyan")

def askForUsername():
    username = input("\n\tEnter your RYM username here: ")
    while username == '' or " " in username:
        cprint("\n\tERROR: Invalid username!", "red")
        username = input("\n\tPlase enter your username again: ")
    return username

def generateRandPageNum():
    maxUserPages = int(input("\n\tEnter the max number of pages in your RYM Wishlist: "))

    randomPage = random.randint(1, maxUserPages + 1)
    albumNum = random.randint(1,25)

    return randomPage, albumNum

def createURL(uname, rPage):
    url = (f"https://rateyourmusic.com/collection/{uname}/r0.0/{rPage}")
    return url

def showInfoandOpen(name, rpg, ralbm, link):

    cprint(f"\n\t>>> YOUR RYM USERNAME: {name}", "cyan")
    cprint(f"\t>>> THE CHOSEN PAGE NUMBER IS: {rpg}", "cyan")
    cprint(f"\t>>> THE RANDOM ALBUM NUMBER IS: {ralbm}", "cyan")

    print("\n\tHope you enjoy this album! :D")
    input("\n\t<<< PRESS [ENTER] TO OPEN THE LINK...")
    webbrowser.open(link)


def main():

    # Ask for number of pages and generate random page and album number
    randPage, randAlbum = generateRandPageNum()

    # Create a url for the random page selected

    url = createURL(accountName, randPage)

    # Display username, page num and album num (and album name) and open the url

    showInfoandOpen(accountName, randPage, randAlbum, url)

################## MAIN

# Show purpose
showPurpose()
# Ask for username
accountName = askForUsername()

continueLetters = ['Y', 'y']
continuePrompt = "Y"
while continuePrompt in continueLetters:
    main()
    continuePrompt = input("\n\tDo you wish to generate another album (Y\\N)?: ")
