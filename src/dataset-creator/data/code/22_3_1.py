def delete_char_at_index(s: str, index: int) -> str:
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    test_string = "Hello World"
    remove_index = 5
    result = delete_char_at_index(test_string, remove_index)
    print(result)