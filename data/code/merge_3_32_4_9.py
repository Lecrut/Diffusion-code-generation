def total_string_length(strings):
    """
    Calculates the total combined length of all strings in a list.
    
    Args:
        strings (list[str]): A list containing string elements.
        
    Returns:
        int: The sum of lengths of all strings in the input list.
    """
    return sum(len(s) for s in strings if isinstance(s, str))

if __name__ == '__main__':
    sample_data = ["hello", "world", "!@#", "", "12345"]
    result = total_string_length(sample_data)
    print(result)  # Output: 16 (5 + 5 + 3 + 0 + 5)