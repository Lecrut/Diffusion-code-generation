def delete_char_at_index(s: str, index: int) -> str:
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    sample_string = "Python"
    target_index = 3
    result = delete_char_at_index(sample_string, target_index)
    print(result)