def reverse_string(input_str: str) -> str:
    """Reverses the order of characters in the input string."""
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or network access is required.
    sample_input = "Hello, World!"
    reversed_result = reverse_string(sample_input)
    print(reversed_result)