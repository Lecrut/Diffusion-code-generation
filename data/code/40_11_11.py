def get_first_letters(strings):
    """
    Returns a list containing only the first character of each non-empty string in the input list.
    
    Args:
        strings (list[str]): A list of strings to process.
        
    Returns:
        list[chr]: A new list with the first letter from each original string.
                   If a string is empty, it contributes an empty element or is skipped based on logic; 
                   here we skip empty strings as per typical "first character" expectations unless specified otherwise.
    
    Note: This implementation uses list comprehension for efficiency and handles edge cases like empty input lists.
    """
    return [s[0] if s else '' for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, no network)
    sample_data = ["hello", "world", "", "python", "!"]
    
    result = get_first_letters(sample_data)
    
    print("Input:", sample_data)
    print("Output:", list(result))