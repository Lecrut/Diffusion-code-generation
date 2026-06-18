def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string using 
    Python's optimized built-in method.
    
    Args:
        phrase (str): The input string to measure.
        
    Returns:
        int: The length of the string in characters.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "12345",
        "Special chars: !@#$%^&*()"
    ]

    print("Sample phrase lengths:")
    for sample in samples:
        length = calculate_phrase_length(sample)
        print(f"'{sample}' -> {length} characters")