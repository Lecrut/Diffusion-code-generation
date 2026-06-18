def get_first_letters(strings):
    """
    Returns a new list containing only the first character of each string in the input list.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A list where each element is the first character of the corresponding input string.
        
    Raises:
        ValueError: If any string in the list is empty or None.
    """
    return [s[0] for s in strings if isinstance(s, str) and len(s) > 0]

if __name__ == '__main__':
    sample_data = ["hello", "world", "python", "code"]
    result = get_first_letters(sample_data)
    print(result)