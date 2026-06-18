def remove_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(' ', '')

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "   Leading and trailing ",
        "NoSpacesHere",
        "A B C D E"
    ]
    
    for test_input in test_cases:
        result = remove_spaces(test_input)
        print(f'Input: {test_input!r} -> Output: {result!r}')