def get_first_letters(strings):
    """
    Iterates through a list of strings and returns a new list containing 
    the first character (lowercased) from each non-empty string, or None 
    if the string is empty.
    
    Args:
        strings (list[str]): A list of input strings.
        
    Returns:
        list[None | str]: A list corresponding to the inputs with only the 
                          first letter of valid strings.
    """
    result = []
    for s in strings:
        if len(s) > 0:
            # Normalize case by converting directly during iteration and lowercasing
            result.append(str(s)[0].lower())
        else:
            # Append None or empty string representation as needed; 
            # here we use an empty string to indicate no character exists.
            result.append("") if s is not None else "" 

    return result

if __name__ == '__main__':
    sample_data = ["Python", "Data Science", "", "Algorithms"]
    
    first_letters = get_first_letters(sample_data)
    print("First letters:", [x for x in first_letters])