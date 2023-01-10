# Printing Heading of Project
print("______________________________________")
print("Python Project to print Acronym")
# Defining Function to create Acronym

''' The program will take input from user and split the strings into world. It will then take first letter
and display it as Acronym'''


def acronymprogram():
    list1 = list(map(str,input("Enter The String:").split()))
    output = ""
    # Iterating the list and getting word one at a time
    for word in list1:
        # Taking first letter of a word and concatenating it with output string
        # and is not considered in acronyms
        if word!="and" or word.upper()!="AND":
            output += word[0]
    # Changing Output's case tp Upper-case
    print ("The acronym for the given string is:",output.upper())
    print("Thank you for using our Acronym Program")
    print("______________________________________")
# Function is called here to execute the acronym function
acronymprogram()