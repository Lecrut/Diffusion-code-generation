def get_first_letters(strings):
    """
    Returns a list containing the first character of each input string.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A list where each element is the first letter 
                   corresponding to the respective input string.
                   
    Raises:
        ValueError: If an empty string or None is encountered in the list,
                    as we cannot determine a 'first' character from them.
    """
    if not strings:
        return []

    result = []
    
    for s in strings:
        # Explicitly handle edge cases to ensure robustness per task requirements
        if not isinstance(s, str) or len(s) == 0:
            raise ValueError(f"Cannot extract a first letter from '{s}'. Please provide non-empty strings.")
        
        result.append(s[0])
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no user input, stdin, or args)
    sample_strings = ["Hello", "World", "Python", "", "Script"]