import string
import random

def generate_list():

    list_of_letters=list(string.ascii_lowercase)
    number_of_letter = len(list_of_letters)
    main_list = []
    
    while number_of_letter > 0:
        a = random.randint(4, 7)
        number_of_letter -= a
        main_list.append(list_of_letters[0:a])
        del list_of_letters[0:a]

    print(main_list)
            
generate_list()