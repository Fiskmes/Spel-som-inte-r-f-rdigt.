import sys
 
hit = 20
Fight = input("Player 1 do you want to hit, flee or do nothing?")

if Fight == "hit":
    print("Your opponent took 20 dmg, your opponent has 80 hp left.")

if Fight == "flee":
    print("The match is over!")
    sys.exit()

if Fight == "do nothing":
    print("You did nothing :/")
    
Fight = input("Player 2 do you want to hit, flee or do nothing?")

