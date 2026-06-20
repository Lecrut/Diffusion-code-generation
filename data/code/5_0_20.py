def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    samples = [
        "hello world",
        "HELLO WORLD",
        "hELLO wORLD",
        "",
        "a",
        "123abc",
        "   spaces"
    ]
    for sample in samples:
        print(capitalize_first_letter(sample))