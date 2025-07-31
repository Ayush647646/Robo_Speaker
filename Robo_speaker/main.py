import os

if __name__ == '__main__':
    print("Welcome to the ROBO SPEAKER 1.1. Created by Ayushman")
    while True:
        x = input("What do you want me to speak? ")
        if x == "exit":
            os.system("say 'Bye bye my friend' ")
            break
        command = f"say {x}"
        os.system(command)


