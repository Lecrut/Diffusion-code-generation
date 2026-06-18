def get_first_letters(string_list):
    """
    Returns a list containing the first letter of each string in the input list.
    
    Args:
        string_list (list[str]): A list of strings to process.
        
    Returns:
        list[str]: A new list with only the first character from each original string.
                   If an empty string is encountered, it returns None for that position.
    """
    result = []
    
    # Iterate through each item in the input list using a clear loop structure
    for s in string_list:
        if len(s) > 0:
            result.append(s[0])
        else:
            result.append(None)
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files needed)
    sample_strings = ["Python", "is", "fun!", "", "Robust"]
    
    first_letters = get_first_letters(sample_strings)
    
    print("Original strings:", sample_strings)
    print("First letters:", first_letters)