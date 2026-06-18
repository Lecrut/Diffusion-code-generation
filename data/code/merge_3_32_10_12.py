def calculate_string_length(text):
    """
    Calculates the total character length of a string, including spaces 
    and punctuation.

    Args:
        text (str): The input string to measure.

    Returns:
        int: The length of the string.
    """
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    # No user input, command-line arguments, or external dependencies used here.
    sample_strings = [
        "Hello World",
        "!@#$%^&*()",
        "",
        "1234567890"
    ]

    for s in sample_strings:
        length = calculate_string_length(s)
        print(f"'{s}' has a total character length of {length}.")