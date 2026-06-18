def get_string_length(s: str) -> int:
    """Return the length of a string using Python's built-in len() function."""
    return len(s)

if __name__ == '__main__':
    sample_strings = ["", "Hello, World!", "", "Python"]
    for test_str in sample_strings:
        print(f"Length of '{test_str}': {get_string_length(test_str)}")