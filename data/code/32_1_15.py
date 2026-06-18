def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string using Python's built-in len() function,
    which is optimized in CPython and highly efficient for this purpose.

    Args:
        phrase (str): The input string to measure.

    Returns:
        int: The length of the string as an integer.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    samples = [
        "Hello, World!",
        "",
        "A" * 10000,
        "Python is optimized.",
    ]

    for phrase in samples:
        length = calculate_phrase_length(phrase)
        print(f"'{phrase}' -> Length: {length}")