def calculate_string_length(string: str) -> int:
    """
    Calculates the total character length of a given string,
    including all spaces, punctuation, and other characters.

    Args:
        string (str): The input string to measure.

    Returns:
        int: The total number of characters in the string.
    """
    return len(string)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or network access is used here.

    test_strings = [
        "Hello World",              # Standard sentence with space
        "Python3!@#",               # Contains letters and punctuation
        ""                          # Empty string case
    ]