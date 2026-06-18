def calculate_total_length(text: str) -> int:
    """Calculate the total character length of a string including spaces and punctuation."""
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or network access is required.
    test_cases = [
        "Hello World!",
        "",
        "Python3",
        "!@#$%^&*()",
    ]

    for text in test_cases:
        result = calculate_total_length(text)
        print(f"Input: '{text}'")
        print(f"Total character length (including spaces and punctuation): {result}")