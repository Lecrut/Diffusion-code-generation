def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_values = ["hello world", "PYTHON", "alreadyCap", "123abc", ""]
    for s in sample_values:
        print(capitalize_first_letter(s))