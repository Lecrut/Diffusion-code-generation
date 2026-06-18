def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the length of a given string (phrase).
    
    This function returns the number of characters in the input string,
    which is O(n) where n is the length of the string. Python's built-in 
    len() function implements this operation efficiently using C-level code.

    Args:
        phrase (str): The string whose length needs to be calculated.

    Returns:
        int: The number of characters in the input string.
    
    Example:
        >>> calculate_phrase_length("Hello")
        5
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction is required
    samples = [
        "Python",
        "",
        "The optimized function adheres to best practices.",
        "Hello, World!",
        1234567890 * "x"  # Large string test for performance verification
    ]

    print("Testing calculate_phrase_length:")
    for sample in samples:
        length = calculate_phrase_length(sample)
        print(f'Sample input len={len(str(sample))} -> Function result {length}')