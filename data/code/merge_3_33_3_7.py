def remove_spaces(s: str) -> str:
    return s.replace(' ', '')

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "  Multiple   Spaces ",
        "",
        "NoSpacesHere",
        "Python Is Great!"
    ]
    
    for case in test_cases:
        result = remove_spaces(case)
        print(f"Input: {case!r} -> Output: {result!r}")