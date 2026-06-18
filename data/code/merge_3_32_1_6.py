def calculate_phrase_length(phrase: str) -> int:
    """
    Returns the total character count of the input string using Python's built-in len().
    
    Args:
        phrase (str): The input string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "12345",
        "!@#$%^&*()",
    ]

    for phrase in samples:
        length = calculate_phrase_length(phrase)
        print(f"Phrase: '{phrase}' -> Length: {length}")