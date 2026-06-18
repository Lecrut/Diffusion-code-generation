def remove_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "  Multiple   Spaces  ",
        "NoSpacesHere",
        "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    ]
    
    for case in test_cases:
        result = remove_spaces(case)
        print(f'Input: {case!r} -> Output: {result!r}')