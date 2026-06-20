def capitalize_if_alphanumeric(text):
    if not text:
        return text
    first_char = text[0]
    if first_char.isalnum():
        return first_char.upper() + text[1:]
    return text

if __name__ == '__main__':
    sample_strings = ["hello world", "123abc", "!special", "", "test123", "42", "_underscore"]
    for s in sample_strings:
        print(capitalize_if_alphanumeric(s))