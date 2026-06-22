def has_non_alphanumeric_non_space(s: str) -> bool:
    for char in s:
        if not (char.isalnum() or char == ' '):
            return True
    return False

if __name__ == '__main__':
    test_strings = ["Hello World", "Hello, World!", "Test123", "NoSpaceHere"]
    for s in test_strings:
        result = has_non_alphanumeric_non_space(s)
        print(result)