def remove_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    original_string = "Hello World"
    char_index_to_remove = 5
    result = remove_char_at_index(original_string, char_index_to_remove)
    print(f"Original: {original_string}")
    print(f"Modified: {result}")