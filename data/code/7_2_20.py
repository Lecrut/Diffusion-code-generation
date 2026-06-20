def contains_special_chars(text):
    special_chars = {
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`'
    }
    text_set = set(text)
    return bool(text_set.intersection(special_chars))

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = contains_special_chars(sample_text)
    print(result)