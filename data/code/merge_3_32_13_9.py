def get_string_length(s: str) -> int:
    """Return the length of a given string."""
    return len(s)

if __name__ == '__main__':
    test_cases = ["", "hello", "Python 3.10"]
    for case in test_cases:
        print(f"Length of '{case}' is {get_string_length(case)}")