def get_first_letters(strings):
    """
    Returns a list containing the first letter of each input string.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A list where each element is the first character 
                   corresponding to the respective input string.
                   
    Raises:
        ValueError: If any string in the list is empty or None.
    """
    result = []
    
    for s in strings:
        if not isinstance(s, str) or len(s) == 0:
            raise ValueError(f"Empty or invalid input found: {s}")
        
        # Efficiently access and append the first character
        result.append(s[0])
        
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction)
    sample_strings = ["Hello", "World", "Python", "Scripting"]
    
    try:
        first_letters = get_first_letters(sample_strings)
        print(first_letters)
    except ValueError as e:
        print(f"Error processing input: {e}")