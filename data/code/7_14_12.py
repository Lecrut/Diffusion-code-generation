def has_special_characters(text, special_chars):
    return bool(set(text) & special_chars)

if __name__ == '__main__':
    SAMPLE_TEXT = "Hello! World"
    SPECIAL_CHARS = {'!', '@', '#', '$', '%'}
    result = has_special_characters(SAMPLE_TEXT, SPECIAL_CHARS)
    print(result)