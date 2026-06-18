def remove_char_at_index(s: str, index: int) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    test_string = "Hello World"
    index_to_remove = 5
    result = remove_char_at_index(test_string, index_to_remove)
    print(f"Original: {test_string}")
    print(f"Removed char at index {index_to_remove}:")
    print(result)