def remove_char_at_index(s: str, index: int) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not (0 <= index < len(s)):
        raise IndexError("Index out of range")
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    test_string = "Hello, World!"
    char_index = 7
    result = remove_char_at_index(test_string, char_index)
    print(f"Original: {test_string}")
    print(f"Removed character at index {char_index}: '{result}'")