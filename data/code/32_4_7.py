def total_string_length(strings):
    """
    Calculates the total combined length of all strings in a list.
    
    Args:
        strings (list[str]): A list containing string elements.
        
    Returns:
        int: The sum of lengths of all strings in the input list.
    """
    return sum(len(s) for s in strings)

if __name__ == '__main__':
    sample_data = ["hello", "world", "", "python", "is", "fun"]
    result = total_string_length(sample_data)
    print(result)  # Expected output: 20 (5 + 5 + 0 + 6 + 1 + 3)