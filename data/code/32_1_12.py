def calculate_phrase_length(text: str) -> int:
    """
    Calculates the total character count of a given string using Python's built-in len().
    
    Args:
        text (str): The input string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, no user interaction needed
    samples = [
        "Hello World",
        "",  # Empty string case
        "!@#$%",  # Special characters
        "Python is awesome!\n"  # Includes newline character
    ]

    for phrase in samples:
        length = calculate_phrase_length(phrase)
        print(f"'{phrase}' -> Length: {length}")