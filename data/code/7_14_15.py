def has_special_chars(text, special_set):
    chars_in_text = set(text)
    return bool(chars_in_text & special_set)

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    predefined_special = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '~', '`'}
    result = has_special_chars(sample_string, predefined_special)
    print(result)