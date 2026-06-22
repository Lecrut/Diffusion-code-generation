def capitalize_first_letter(s):
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "  python programming ",
        "",
        "ALREADY CAPTURED",
        "123numbers"
    ]
    
    for value in sample_values:
        print(capitalize_first_letter(value))