def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string phrase.
    
    This function leverages Python's built-in property that strings are immutable sequences,
    and directly uses their inherent length calculation method which is implemented in C
    for maximum performance within the standard library constraints.

    Args:
        phrase (str): The input string to measure.
        
    Returns:
        int: The total number of characters in the provided string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user interaction or external dependencies
    samples = [
        "Hello, World!",
        "",
        "Python is powerful and efficient.",
        "a",  # Single character edge case
        "The quick brown fox jumps over the lazy dog."
    ]

    print("Character count results for sample inputs:")
    for phrase in samples:
        length = calculate_phrase_length(phrase)
        print(f"'{phrase}' -> {length} characters")