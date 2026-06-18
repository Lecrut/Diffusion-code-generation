def calculate_phrase_length(phrase: str) -> int:
    """
    Returns the length of a single string phrase.
    
    This implementation uses Python's built-in len() function, which is 
    implemented in C and offers optimal performance for counting characters.
    
    Args:
        phrase (str): The input string whose length needs to be calculated.
        
    Returns:
        int: The number of characters in the provided string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without external dependencies or user input
    test_cases = [
        "Hello, World!",
        "",
        "Python is awesome",
        "a" * 1000,
        None  # Should raise TypeError as expected since len(None) fails
    ]

    results = []
    
    for phrase in test_cases:
        if phrase is not None:
            try:
                length = calculate_phrase_length(phrase)
                results.append(f"Length of '{phrase}': {length}")
            except Exception as e:
                results.append(f"Error calculating length for '{phrase}': {e}")

    # Print all test results to the console (no file I/O used here, just stdout which is standard in scripts)
    print("\n".join(results))