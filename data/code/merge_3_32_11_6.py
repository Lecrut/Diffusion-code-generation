def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the length of a given string (phrase).
    
    This function uses Python's built-in len() which is implemented in C,
    making it highly efficient for counting characters. It adheres to 
    best practices by using type hinting and avoiding unnecessary operations.

    Args:
        phrase (str): The input string whose length needs to be calculated.

    Returns:
        int: The number of characters in the provided string.
    
    Example:
        >>> calculate_phrase_length("Hello, World!")
        13
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Python is awesome",
        "",
        "A",
        "The quick brown fox jumps over the lazy dog!",
        None  # Should raise TypeError as expected for non-string inputs
    ]

    print("Testing calculate_phrase_length function:")
    
    for sample in samples:
        if sample is not None and isinstance(sample, str):
            try:
                result = calculate_phrase_length(sample)
                print(f"Input: {sample!r} -> Length: {result}")
            except Exception as e:
                print(f"Error processing input {sample!r}: {e}")
        elif sample is None:
            print("Testing with None (expected to raise TypeError):")
            try:
                result = calculate_phrase_length(sample)
                print(f"Unexpected success: {result}")
            except TypeError as e:
                print(f"Correctly raised TypeError: {e}")
        else:
            print(f"Skipping non-string input type: {type(sample)}")