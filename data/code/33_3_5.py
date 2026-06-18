def remove_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(" ", "")

if __name__ == '__main__':
    samples = [
        "Hello World",
        "  Leading and trailing   ",
        "NoSpacesHere123",
        "Multiple   Spaces   In   The   Middle"
    ]
    
    for sample in samples:
        result = remove_spaces(sample)
        print(f'Input: {sample!r} -> Output: {result!r}')