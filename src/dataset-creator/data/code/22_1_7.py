def remove_char_at_index(s: str, index: int) -> str:
    return s[:index] + s[index+1:] if 0 <= index < len(s) else s
if __name__ == '__main__':
    original = "Hello World"
    result = remove_char_at_index(original, 5)
    print(f"Original: {original}")
    print(f"Modified: {result}")