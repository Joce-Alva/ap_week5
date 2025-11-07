#a function allows us to bundle code into a reuseable block to make it easier to manage and understand
#by defining functions we can avoid code duplication and enhance reliability 

#define a function
def problem1():
    # Problem Set 1: Indexing and Slicing Strings
    # Basic Indexing:
    # Given the string 
    magic = "abracadabra"
    # a. Retrieve the 5th character.
    print(magic[4])
    # b. Retrieve the second to last character.
    print(magic[-2])
    # c. Find the first occurrence of the letter 'c'.
    first_occurence_c = magic.find('c')
    print(first_occurence_c)
#calling the function 