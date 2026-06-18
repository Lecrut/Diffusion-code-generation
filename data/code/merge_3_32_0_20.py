def calculate_string_length(s: str) -> int:
    """
    Calculates the length of a given string, handling both ASCII and Unicode characters efficiently.
    
    Args:
        s (str): The input string to measure.
        
    Returns:
        int: The number of code points in the string.
            
    Note:
        Python's built-in len() function already handles Unicode correctly by counting 
        individual code points, not grapheme clusters or bytes. This is more efficient
        than manual iteration for large strings and avoids external dependencies.
        
    Example:
        >>> calculate_string_length("Hello")
        5
        >>> calculate_string_length("こんにちは")
        3
    """
    return len(s)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or network access.
    
    samples = [
        "ASCII Example",
        "Unicode: こんにちは世界",
        "",
        "Mixed: 123 🎉 Привет тест"
    ]

    for test_string in samples:
        length = calculate_string_length(test_string)
        print(f"'{test_string}' has a length of {length} characters.")