def has_special_characters(text, special_chars):
    text_set = set(text)
    special_set = set(special_chars)
    return len(text_set & special_set) > 0

if __name__ == '__main__':
    sample_text = "Hello, World!"
    predefined_specials = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"}
    result = has_special_characters(sample_text, predefined_specials)
    print(result)