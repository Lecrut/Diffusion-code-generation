def get_string_length(s: str) -> int:
    """Returns the length of a string."""
    return len(s)

if __name__ == '__main__':
    test_strings = ["hello", "", "Python 3.12"]
    for s in test_strings:
        print(f"Length of '{s}' is {get_string_length(s)}")