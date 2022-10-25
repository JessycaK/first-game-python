#Role playing game
#Choose an option to advance in the game
#You decide where you go and what to do
#The quest is to choose the best option that will keep you alive

print("Welcome to survival world!")
print("Let the adventure begin!!! ")
name = input("What is your name ? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
  print("You are old enough to play? ")

  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("You are starting with", health, "health")
    print("let's play!")

    left_or_right = input("First choice... Left or Right (left/right? ")

    if left_or_right == "left":
      ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around) ")

      if ans == "around":
          print("You went around and reached a lake... Do you swim across or go around (across/around)? ")
      elif ans == "across":
            print("You managed to get across, but were bit by a fish and lost 5 health.")
            health -= 5

      ans = input("You notice a house and a river. Which do you go to (river/house)?")

      if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")
      else:
          print("You fell in the river and lost...")


    else:
        print("You fell down and lost...")

  else:
      print("Cya...")
else:
    print("You are not old enough to play...")


