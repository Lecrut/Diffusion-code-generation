def capitalize_first_letter(text):
    if not text:
        return ""
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "python programming",
        "capitalize this!",
        "",
        "123abc",
        "already Capitalized",
        "punctuation: should, remain; intact."
    ]
    
    for value in sample_values:
        print(capitalize_first_letter(value))