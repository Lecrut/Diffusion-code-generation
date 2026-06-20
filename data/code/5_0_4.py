def capitalize_first_letter(text):
    if not text:
        return ""
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_1 = "hello world"
    sample_2 = "wORLD"
    sample_3 = ""
    sample_4 = "a"
    print(capitalize_first_letter(sample_1))
    print(capitalize_first_letter(sample_2))
    print(capitalize_first_letter(sample_3))
    print(capitalize_first_letter(sample_4))