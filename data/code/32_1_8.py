def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string using Python's built-in len() function,
    which is implemented in C and offers optimal performance compared to manual iteration or slicing.

    Args:
        phrase (str): The input string for which the length needs to be determined.

    Returns:
        int: The total number of characters in the provided string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user input or external dependencies needed.
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "12345",
        "The quick brown fox jumps over the lazy dog."
    ]

    for phrase in samples:
        length = calculate_phrase_length(phrase)
        print(f"Phrase: '{phrase}' -> Length: {length}")