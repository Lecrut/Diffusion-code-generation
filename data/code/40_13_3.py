def get_first_letter(s: str) -> str:
    """Returns the first letter of the input string if it is non-empty, otherwise returns an empty string."""
    return s[0] if len(s) > 0 else ""

if __name__ == '__main__':
    test_cases = ["Hello", "", "Python"]
    for case in test_cases:
        print(f"Input: {repr(case)} -> Output: {repr(get_first_letter(case))}")