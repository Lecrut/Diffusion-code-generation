def reverse_word(text: str) -> str:
    """Returns the reversed version of a single string."""
    return text[::-1]

if __name__ == '__main__':
    test_cases = [
        "hello",
        "Pythonic code",
        "",
        "a"
    ]

    for case in test_cases:
        print(f"Original: {case!r} -> Reversed: {reverse_word(case)!r}")