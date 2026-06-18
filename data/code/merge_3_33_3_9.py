def remove_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(" ", "")

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "  Leading and Trailing Spaces  ",
        "NoSpacesHere",
        "Multiple   Spaces   Between"
    ]
    
    for test_input in sample_strings:
        result = remove_spaces(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')