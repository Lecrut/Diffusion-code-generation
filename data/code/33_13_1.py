def remove_spaces(s: str) -> str:
    """Returns a new string with all spaces removed."""
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = ["Hello World", "  Multiple   Spaces  ", "NoSpacesHere"]
    for case in test_cases:
        result = remove_spaces(case)
        print(f"Input: {case!r} -> Output: {result!r}")