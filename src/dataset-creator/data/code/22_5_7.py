def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, (int)) and not isinstance(index, bool):
        raise TypeError("Index must be an integer.")
    if index < 0 or index >= len(s):
        return s
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    sample_string = "Hello, World!"
    target_index = 7
    result = delete_char_at_index(sample_string, target_index)
    print(f"Original: {sample_string}")
    print(f"Deleted char at index {target_index}: '{result}'")