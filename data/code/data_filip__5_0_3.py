def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    samples = ["hello", "WORLD", "hELLO wORLD", "python", "", "a", "123abc"]
    for sample in samples:
        print(capitalize_first_letter(sample))