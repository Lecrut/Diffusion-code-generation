def get_first_letters(strings):
    """
    Returns a list containing the first character of each string in the input list.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[chr]: A new list with the first letter from each original string.
    """
    return [s[0] for s in strings if len(s) > 0]

if __name__ == '__main__':
    sample_data = ["hello", "world", "!python", "" , "test"]
    result = get_first_letters(sample_data)
    
    # Note: The empty string is filtered out to prevent IndexError, 
    # ensuring robustness while maintaining the core logic of extracting first letters.
    print(result)