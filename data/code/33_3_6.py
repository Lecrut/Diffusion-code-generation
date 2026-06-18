def remove_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = [
        "  Hello World!   ",
        "NoSpacesHere",
        "One Two Three Four Five",
        "",
        " Multiple   Spaces ",
    ]

    for input_str in test_cases:
        result = remove_spaces(input_str)
        print(f"Input: {input_str!r} -> Output: {result!r}")