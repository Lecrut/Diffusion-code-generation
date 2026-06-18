def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string using Python's built-in len() function,
    which is implemented in C and offers optimal performance compared to manual iteration or slicing.

    Args:
        phrase (str): The input string whose length needs to be determined.

    Returns:
        int: The number of characters in the provided string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "A" * 1000,
        None if False else ""  # Ensuring type hint safety while keeping logic simple
    ]

    for sample in samples:
        length = calculate_phrase_length(sample)
        print(f"'{sample}' has {length} character(s).")