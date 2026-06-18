def calculate_phrase_length(phrase: str) -> int:
    """
    Calculate the length of a given string (phrase).
    
    This function simply returns the number of characters in the input string,
    which is an O(n) operation inherent to Python's built-in len() function.
    Using the optimized C implementation of len() ensures maximum efficiency 
    and adherence to Python best practices for performance-critical operations.

    Args:
        phrase (str): The input string whose length needs to be calculated.

    Returns:
        int: The number of characters in the provided string.
    
    Examples:
        >>> calculate_phrase_length("Hello")
        5
        >>> calculate_phrase_length("")
        0
    """
    return len(phrase)

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    sample_phrases = [
        "Python is awesome",
        "",
        "A" * 100,
        "The quick brown fox jumps over the lazy dog."
    ]

    for phrase in sample_phrases:
        length = calculate_phrase_length(phrase)
        print(f'Phrase: "{phrase}" -> Length: {length}')