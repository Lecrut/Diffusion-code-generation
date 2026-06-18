def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the length of a given string (phrase).
    
    This function uses Python's built-in len() which is implemented in C,
    making it highly efficient for counting characters. It adheres to 
    best practices by using type hinting and avoiding unnecessary operations.

    Args:
        phrase (str): The input string whose length needs to be calculated.

    Returns:
        int: The number of characters in the provided string.
    
    Examples:
        >>> calculate_phrase_length("Hello")
        5
        >>> calculate_phrase_length("")
        0
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Python is awesome",
        "",
        "A",
        "The quick brown fox jumps over the lazy dog"
    ]

    for phrase in samples:
        length = calculate_phrase_length(phrase)
        print(f"'{phrase}' has a length of {length}.")