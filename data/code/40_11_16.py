def get_first_letters(strings):
    """
    Returns a new list containing only the first character of each non-empty string in the input list.
    
    Args:
        strings (list[str]): A list of strings to process.
        
    Returns:
        list[str]: A list of single-character strings, where each element is the first character 
                   corresponding to a non-empty string from the input list. Empty strings are skipped.
    """
    return [s[0] for s in strings if len(s) > 0]

if __name__ == '__main__':
    sample_data = ["hello", "world", "!@#", "", "python"]
    result = get_first_letters(sample_data)
    print(result)