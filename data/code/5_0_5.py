def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "HELLO WORLD",
        "hELLO wORLD",
        "",
        "a",
        "123abc",
        "python programming"
    ]
    for sample in sample_values:
        result = capitalize_first_letter(sample)
        print(result)