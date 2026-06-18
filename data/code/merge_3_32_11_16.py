def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the length of a given string.

    This function uses Python's built-in len() function, which is implemented in C
    and provides optimal performance by directly computing memory size without
    character-by-character iteration or complex logic.

    Args:
        phrase (str): The input string whose length needs to be determined.

    Returns:
        int: The total number of characters in the provided string, including
             whitespace and special characters but excluding any surrounding quotes.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [
        "Hello",
        "",
        "Python is awesome!",
        "The quick brown fox jumps over the lazy dog.",
        "!@#$%^&*()_+{}[]:"
    ]

    for phrase in samples:
        length = calculate_phrase_length(phrase)
        print(f"Phrase: '{phrase}' -> Length: {length}")