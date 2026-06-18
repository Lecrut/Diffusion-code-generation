def calculate_string_length(input_str):
    """Calculates the total character length of a given string, including spaces and punctuation."""
    return len(input_str)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or network access is required.
    test_strings = [
        "Hello World!",
        "123-456",
        "",
        "...!!!?"
    ]

    for s in test_strings:
        length = calculate_string_length(s)
        print(f"Input string length: {length}")