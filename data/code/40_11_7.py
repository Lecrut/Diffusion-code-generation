def get_first_letters(strings):
    """
    Returns a new list containing only the first character of each string in the input list.
    
    Parameters:
        strings (list[str]): A list of strings to process.
        
    Returns:
        list[chr]: A list where each element is the first character of the corresponding input string.
                   If an empty string is present, it will result in an empty string being included.
    """
    return [s[0] if s else '' for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_strings = ["hello", "world", "", "python"]
    
    result = get_first_letters(sample_strings)
    
    print("Input list:", sample_strings)
    print("Output list of first letters:", result)