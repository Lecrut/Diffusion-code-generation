def reverse_string(s: str) -> str:
    """Reverses a given string using Python's built-in slice notation."""
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "Python is great.", "!dlroW ,olleH"]

    for test_input in sample_strings:
        print(f"Original String: '{test_input}'")
        reversed_output = reverse_string(test_input)
        print("Reversed String:", reversed_output)