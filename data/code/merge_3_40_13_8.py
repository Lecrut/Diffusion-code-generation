def get_first_letter(input_string: str) -> str:
    """Returns the first letter of the input string if it exists, otherwise returns an empty string."""
    return input_string[0] if len(input_string) > 0 else ""

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "",
        "a",
        "   leading spaces"
    ]

    for case in test_cases:
        result = get_first_letter(case)
        print(f'Input: {repr(case)} -> Output: {repr(result)}')