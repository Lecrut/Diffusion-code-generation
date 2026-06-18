def remove_all_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(" ", "")

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "  Multiple   Spaces  ",
        "NoSpacesHere",
        "Python Programming"
    ]
    
    for test_str in sample_strings:
        result = remove_all_spaces(test_str)
        print(f'"{test_str}" -> "{result}"')