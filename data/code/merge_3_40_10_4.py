def get_first_letters(strings):
    """
    Returns a list containing the first character of each input string.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A list of single-character strings representing 
                   the first letter of each input string.
                   
    Raises:
        ValueError: If any element in the list is not a string or is empty.
    """
    result = []
    
    for s in strings:
        if not isinstance(s, str):
            raise TypeError(f"Expected a string but got {type(s).__name__}")
        
        if len(s) == 0:
            raise ValueError("Empty string provided")
            
        # Efficiently access the first character using index slicing or direct indexing
        result.append(s[0])
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, etc.)
    sample_data = ["Python", "DataScience", "RobustCode"]
    
    first_letters = get_first_letters(sample_data)
    
    print(first_letters)