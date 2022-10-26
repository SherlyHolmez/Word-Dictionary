import json
from PyDictionary import PyDictionary

dictionary = PyDictionary()
def main():
    choice = input("Would you like to use the word dictionary (Y/N) :").lower()

    if choice == 'y':

        while True:
            word = input("Please enter the word you would like to check in the dictionary:\n")
            if dictionary.meaning(word, disable_errors=True):
                print("The definition of ", word," is: ")
                formatted_result =  json.dumps(dictionary.meaning(word), indent=4)

                print(formatted_result)
                print("")
                print("-----------------------------------------------")
                selection = input("Do you want to check another word? (Y/N) :").lower()
                while selection!= 'y':
                    if selection == 'n':
                        print("Thanks for using the dictionary!")
                        exit()
                    else:
                        print("Invalid choice")
                        selection = input("Do you want to check another word? (Y/N) :").lower()
            else:
                print("Word Not Found")

    if choice=='n':
        print("Thanks for using the dictionary!")
        exit()
    else:
        print("Invalid choice")
        main()


main()