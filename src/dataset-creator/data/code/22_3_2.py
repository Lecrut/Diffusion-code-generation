def delete_char_at_index(s: str, index: int) -> str:
    if not (0 <= index < len(s)):
        raise IndexError("Index out of bounds")
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    input_string = "Python"
    target_index = 3
    result = delete_char_at_index(input_string, target_index)
    print(result)