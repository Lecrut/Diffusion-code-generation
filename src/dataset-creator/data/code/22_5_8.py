def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(s):
        return s
    result = s[:index] + s[index+1:]
    return result
if __name__ == '__main__':
    sample_string = "Hello, World!"
    target_index = 5
    output = delete_char_at_index(sample_string, target_index)
    print(f"Original: {sample_string}")
    print(f"After deleting character at index {target_index}: {output}")