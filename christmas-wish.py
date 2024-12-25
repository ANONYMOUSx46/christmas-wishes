import time 
import random

#Define a list of christmas wishes
wishes = [
    "Merry Christmas!",
    "May your Christmas be filled with Love, Joy and Peace.",
    "May the lord Jesus Christ grant you the gifts of health, wealth and wisdom.",
    "Wishing you a ver Merry Christmas and happy New Year!!!",
    "May all your Christmas dreams come true!"
]

#Define a list of Christmas colours
colors = [
    "\033[31m", #red
    "\033[32m", #green
    "\033[33m", #yellow
    "\033[34m", #blue
    "\033[35m", #magenta
    "\033[36m", #cyan
    "\033[37m" #white
]

#print a christmas tree
print("""
          .     .  .      +     .      .          .
     .       .      .     #       .           .
        .      .         ###            .      .      .
      .      .   "#:. .:##"##:. .:#"  .      .
          .      . "####"###"####"  .
       .     "#:.    .:#"###"#:.    .:#"  .        .       .
  .             "#########"#########"        .        .
        .    "#:.  "####"###"####"  .:#"   .       .
     .     .  "#######""##"##""#######"                  .
                ."##"#####"#####"##"           .      .
    .   "#:. ...  .:##"###"###"##:.  ... .:#"     .
      .     "#######"##"#####"##"#######"      .     .
    .    .     "#####""#######""#####"    .      .
            .     "      000      "    .     .
       .         .   .   000     .        .       .
.. .. ..................O000O........................ ...... ...""")

#get name of  the person to wish
name = input("Enter your name please:")

#send Christmas wishes to the person
for wish in wishes:
    #randomly select the color
    color = random.choice(colors)

    #print the wish with the selected color 
    print(color + f"{wish}, {name}")

    #reset the color to white
    print("\033[0m")

    #wait for a sec
    time.sleep(1)

#print a message
print("wishing you all the best for Christmas and New Year!")