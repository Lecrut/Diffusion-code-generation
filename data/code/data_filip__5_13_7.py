def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "", "a", "already Capitalized"]
    for sample in sample_strings:
        result = capitalize_first_letter(sample)
        print(result)