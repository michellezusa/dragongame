
print("Welcome to the Magical Forest!")

name = input("What is your name? ")

print("Hello,", name)
print("A baby dragon is lost in the forest!")
print("Your mission is to find it.")

path = input("Go LEFT or RIGHT? ").lower()

if path == "left":
    print("You found a sparkling river!")

    choice = input("SWIM or BRIDGE? ").lower()

    if choice == "bridge":
        print("You crossed safely!")
        print("You found the baby dragon!")
        print("YOU WIN!")
    else:
        print("Oh no! The river is too strong!")
        print("GAME OVER!")

elif path == "right":
    print("You meet a sleeping giant owl!")

    choice = input("SING or RUN? ").lower()

    if choice == "sing":
        print("The owl loves your song!")
        print("It shows you where the dragon is!")
        print("YOU WIN!")
    else:
        print("The owl wakes up and scares you!")
        print("GAME OVER!")

else:
    print("You got lost in the forest!")
