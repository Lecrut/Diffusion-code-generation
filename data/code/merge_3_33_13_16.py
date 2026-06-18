def remove_spaces(s: str) -> str:
    """Returns a copy of the string with all spaces removed."""
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = ["hello world", "no  sp   aces here", " "]
    for case in test_cases:
        result = remove_spaces(case)
        print(f"Input: {case!r} -> Output: {result!r}")