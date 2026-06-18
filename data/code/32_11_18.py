def calculate_phrase_length(phrase: str) -> int:
    """
    Calculate the length of a given string (phrase).
    
    This function is optimized by directly returning len(), which is implemented 
    in C within Python and provides O(n) time complexity with minimal overhead.
    
    Args:
        phrase (str): The input string whose length needs to be calculated.
        
    Returns:
        int: The number of characters in the provided string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    samples = [
        "Hello, World!",
        "",
        "Python is great.",
        "a" * 1000,
        None if False else ""  # Ensuring only valid string cases are tested as per requirements
    ]

    for sample in samples:
        result = calculate_phrase_length(sample)
        print(f"Input length of '{sample[:20]}{'...' if len(sample) > 20 else ''}': {result}")