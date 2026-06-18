def get_first_letters(strings):
    """
    Returns a list containing the first character of each non-empty string in the input list.
    
    Args:
        strings (list[str]): A list of string values.
        
    Returns:
        list[str]: A new list with only the first character from each original string.
                   Strings that are empty or None result in no value added for those items.
    """
    return [s[0] if s else '' for s in strings]

if __name__ == '__main__':
    sample_data = ["apple", "banana", "", "cherry"]
    result = get_first_letters(sample_data)
    print(result)  # Output: ['a', 'b', '', 'c']