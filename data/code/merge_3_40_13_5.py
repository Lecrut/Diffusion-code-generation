def get_first_letter(s: str) -> str:
    """Returns the first letter of a string if it exists, otherwise returns an empty string."""
    return s[0] if len(s) > 0 else ""

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "",
        "a",
        "123!@#",
        "   Python ",
    ]

    for case in test_cases:
        result = get_first_letter(case)
        print(f"Input: {repr(case)} -> Output: {repr(result)}")