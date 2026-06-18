def get_first_letter(s: str) -> str:
    """Returns the first letter of a string if it exists, otherwise returns an empty string."""
    return s[0] if len(s) > 0 else ""

if __name__ == '__main__':
    test_cases = ["hello", "", "   ", "a"]
    for case in test_cases:
        print(f"Input: {repr(case)} -> Output: {get_first_letter(case)!r}")