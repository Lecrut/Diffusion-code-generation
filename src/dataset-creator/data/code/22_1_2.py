def remove_char_at_index(s: str, index: int) -> str:
    return s[:index] + s[index+1:] if 0 <= index < len(s) else s
if __name__ == '__main__':
    original = "Hello World"
    char_to_remove = 'o'
    new_string = remove_char_at_index(original, 4)
    print(f"Original: {original}")
    print(f"After removing character at index 4 ('o'): {new_string}")