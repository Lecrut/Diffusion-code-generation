def get_string_length(s: str) -> int:
    """Return the length of a string."""
    return len(s)

if __name__ == '__main__':
    sample_strings = ["hello", "", "Python 3"]
    for s in sample_strings:
        print(f"Length of '{s}' is {get_string_length(s)}")