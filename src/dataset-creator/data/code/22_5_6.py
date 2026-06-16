def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index < 0 or index >= len(s):
        return s
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    sample_string = "Hello, World!"
    delete_index = 7
    result = delete_char_at_index(sample_string, delete_index)
    print(result)