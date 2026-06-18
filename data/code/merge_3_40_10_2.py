def get_first_letters(string_list):
    """
    Reads a list of strings and prints the first letter of each string.
    
    Args:
        string_list (list[str]): A list of input strings.
        
    Prints:
        The first character from each non-empty string in the provided list.
    """
    for item in string_list:
        if len(item) > 0 and isinstance(item, str):
            print(item[0])

def main():
    # Hard-coded sample values as per requirements (no user input or external files needed).
    sample_strings = ["Hello", "Python Programming", "World", "!@#", "" ]

    get_first_letters(sample_strings)

if __name__ == '__main__':
    main()