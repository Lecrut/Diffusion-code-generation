def contains_special_characters(text: str) -> bool:
    special_symbols = {
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\',
        ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~'
    }
    text_chars = set(text)
    return bool(text_chars.intersection(special_symbols))

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = contains_special_characters(sample_text)
    print(result)