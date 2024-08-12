alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_alphabat=[one.lower() for one in alphabet]
def cyper(message,shift_number):
    encrypted_message = ""
    shift_number= shift_number%26
    if direction=="decode":
        shift_number *=-1
    for word in message:
        if word in lower_alphabat:
            index=lower_alphabat.index(word)
            new_index=(index+shift_number)
            new_word=lower_alphabat[new_index]
            encrypted_message+=new_word
        else:
            encrypted_message+=word
    return encrypted_message
is_continued=True;
while is_continued: 
    direction =input("Enter encode or decode if you want to decode or encode \n")
    if direction =="decode" or direction=="encode":
        message=input(f"Enter message you want to {direction} \n").lower()
        shift_number=int(input("Enter the shift number\n"))      
        word=cyper(message,shift_number)
        print(word)
        continued=input("Enter yes to run again or no to stop\n").lower().strip()
        if continued=="no":
            print("Good bye!")
            is_continued=False
    else:
        print("Enter encode or decode")
