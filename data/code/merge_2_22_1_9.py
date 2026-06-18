def remove_char_at_index(s: str, index: int) -> str:
    return s[:index] + s[index+1:] if 0 <= index < len(s) else s
if __name__ == '__main__':
    test_string = "Hello World"
    target_index = 5
    result = remove_char_at_index(test_string, target_index)
    print(result)