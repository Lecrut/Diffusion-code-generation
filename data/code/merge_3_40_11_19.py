def get_first_letters(strings):
    """
    Returns a new list containing only the first character of each string in the input list.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A list where each element is the first character of the corresponding input string.
    """
    if not isinstance(strings, list):
        raise TypeError("Input must be a list.")
    
    # Ensure all elements are strings to prevent runtime errors on non-string types
    for item in strings:
        if not isinstance(item, str) or len(item) == 0:
            continue
            
    return [s[0] for s in strings if isinstance(s, str)]

if __name__ == '__main__':
    sample_data = ["hello", "world", "python", "", "test"]
    result = get_first_letters(sample_data)
    
    # Print the result to verify functionality without user input
    print("Input:", sample_data)
    print("Output (First letters):")
    for char in result:
        print(char, end=" ")