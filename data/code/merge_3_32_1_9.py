def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string using Python's built-in len().
    
    Parameters:
        phrase (str): The input string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or file access
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "12345",
        "!@#$%^&*()_+-=[]{}|;:,.<>?"
    ]

    for sample in samples:
        length = calculate_phrase_length(sample)
        print(f"Phrase: '{sample}' -> Length: {length}")