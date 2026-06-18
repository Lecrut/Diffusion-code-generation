def get_first_letters(strings):
    """
    Returns a new list containing only the first character of each string in the input list.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A list where each element is the first character of the corresponding input string.

    Raises:
        ValueError: If any string in the list is empty or None, as extracting a first letter would fail.
    """
    # Validate inputs to ensure safe extraction without errors for edge cases like empty strings
    if not all(isinstance(s, str) and len(s) > 0 for s in strings):
        raise ValueError("All elements must be non-empty strings.")

    return [s[0] for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "code"]
    result = get_first_letters(sample_strings)
    print(result)  # Output: ['h', 'w', 'p', 'c']