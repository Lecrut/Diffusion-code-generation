def check_unique_chars(text: str) -> bool:
    visited = set()
    for current_char in text:
        if current_char in visited:
            return False
        visited.add(current_char)
    return True

if __name__ == '__main__':
    sample_text = 'hello'
    is_unique = check_unique_chars(sample_text)
    print(is_unique)