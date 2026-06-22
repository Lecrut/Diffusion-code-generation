def has_non_alnum_space(text: str) -> bool:
    for char in text:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_text = "Hello World 123!"
    result = has_non_alnum_space(sample_text)
    print(result)