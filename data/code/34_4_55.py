def capitalize_first_letter(s):
    if not s:
        return ""
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "123abc",
        "",
        "punctuation! is tricky.",
        "multiple words here"
    ]
    
    for value in sample_values:
        print(capitalize_first_letter(value))