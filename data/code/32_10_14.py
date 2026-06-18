def calculate_string_length(text: str) -> int:
    """
    Calculates the total length of a given string, including all characters,
    spaces, punctuation, and special symbols.

    Args:
        text (str): The input string to measure.

    Returns:
        int: The number of characters in the string.
    """
    return len(text)

def main():
    # Hard-coded sample values as per requirements
    # This ensures no user input, command-line arguments, or network access is needed.
    test_strings = [
        "Hello World!",
        "Python 3.12",
        "",
        "!@#$%^&*()",
        "Mixed: spaces   and punctuation"
    ]

    for sample in test_strings:
        length = calculate_string_length(sample)
        print(f'String: "{sample}" -> Length: {length}')

if __name__ == '__main__':
    main()