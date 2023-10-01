from math import sqrt

def encrypt(verse: str) -> str:
    encypt_txt = ''
    for ch in verse:
        encypt_txt += chr((((((ord(ch) * 4) - 2) // 2) + 5) ** 2))
    return encypt_txt

def decrypt(verse: str) -> None:
    main_txt = ""
    for ch in encypt_txt:
        main_txt += chr(round((((int(sqrt((ord(ch)))) - 5) * 2) + 2) // 4))   
    return main_txt 

while True:
    choice = input("enter your choose: \n" + "1.encrypt" + '\n' + "2.decrypt" + '\n' '3.exit' + '\n')
    if choice == '1':
        main_txt = input("enter your txt: ")
        print("encrypted txt: ", encrypt(main_txt))
        print("*" * 40 + '\n')
    
    elif choice == '2':
        encypt_txt = input("enter your encrypted txt: ")
        main_txt = ""
        for ch in encypt_txt:
            main_txt += chr(round((((int(sqrt((ord(ch)))) - 5) * 2) + 2) // 4))
        print("main txt: ", decrypt(main_txt))
        print("*" * 40 + '\n')
    
    elif choice == '3':
        print("good bye!")
        break

    else: print("worng command!")


    