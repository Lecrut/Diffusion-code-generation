def remove_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    original = "Hello World"
    result = remove_char_at_index(original, 5)
    print(f"Original: {original}")
    print(f"Modified: {result}")