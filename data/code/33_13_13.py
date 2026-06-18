def remove_spaces(s: str) -> str:
    """Returns a new string with all spaces removed."""
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = ["Hello World", "Python 3.12", "", "NoSpacesHere"]
    for case in test_cases:
        print(f"Input: {case!r} -> Output: {remove_spaces(case)!r}")