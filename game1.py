def dark_room_game():
    print("You wake up in a dark room. You can see a small door to your right.")
    
    while True:
        action = input("What do you want to do? (1. Look around 2. Open door 3. Shout for help): ").strip()
        
        if action == "1":
            print("It's too dark to see anything else. The door is your best option.")
        elif action == "2":
            print("The door is locked. There might be a key somewhere.")
            while True:
                action = input("What do you want to do? (1. Search for key 2. Kick door): ").strip()
                
                if action == "1":
                    print("You found the key under a loose floorboard!")
                    while True:
                        action = input("Do you want to use the key to open the door? (yes/no): ").strip().lower()
                        
                        if action == "yes":
                            print("You unlocked the door and escaped the room. Congratulations!")
                            return
                        elif action == "no":
                            print("You decide not to use the key. The door remains locked.")
                        else:
                            print("Invalid choice. Please answer 'yes' or 'no'.")
                elif action == "2":
                    print("You hurt your foot! The door is still locked. Try something else.")
                else:
                    print("Invalid choice. Try again.")
        elif action == "3":
            print("No one hears your shouts. The door is still your best option.")
        else:
            print("Invalid choice. Try again.")

dark_room_game()


