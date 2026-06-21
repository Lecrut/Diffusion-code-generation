def capitalize_first_letter(s):
    if not s:
        return ""
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "HELLO WORLD",
        "hello WORLD",
        "hElLo WoRlD",
        "",
        "123abc",
        "!@#abc",
        "a!@#bc"
    ]
    
    for value in sample_values:
        print(capitalize_first_letter(value))