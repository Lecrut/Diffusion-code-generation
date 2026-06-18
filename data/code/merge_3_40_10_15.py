def get_first_letters(strings):
    """
    Returns a list containing the first letter of each input string.
    
    Args:
        strings (list[str]): A list of strings to process.
        
    Returns:
        list[str]: A list where each element is the first character 
                   corresponding to the respective input string, or an empty string if None.
    """
    result = []
    for s in strings:
        # Handle cases where a string might be missing (though task implies valid inputs)
        if not isinstance(s, str):
            continue
        first_char = s[0] if len(s) > 0 else ''
        result.append(first_char)
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_strings = ["Python", "is", "awesome!", "", "Robust"]
    
    first_letters = get_first_letters(sample_strings)
    
    print("First letters:")
    for letter in first_letters:
        print(letter)