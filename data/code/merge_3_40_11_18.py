def get_first_letters(strings):
    """
    Returns a new list containing the first character of each string in the input list.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A list where each element is the first character of the corresponding 
                   input string. If any string is empty, it returns an empty string for that position.
    """
    return [s[0] if s else '' for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_data = ["hello", "world", "", "python"]
    
    result = get_first_letters(sample_data)
    
    print("Input:", sample_data)
    print("Output:", result)