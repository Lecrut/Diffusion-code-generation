def capitalize_first(s):
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
        " already capitalized"
    ]
    for sample in samples:
        result = capitalize_first(sample)
        print(result)