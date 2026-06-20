def capitalize_first_char(text: str) -> str:
    if not text:
        return ""
    return text[0].upper() + text[1:].lower()

if __name__ == '__main__':
    sample1 = "hELLO wORLD"
    sample2 = "python programming"
    sample3 = "a"
    sample4 = "ABC"
    sample5 = ""

    print(capitalize_first_char(sample1))
    print(capitalize_first_char(sample2))
    print(capitalize_first_char(sample3))
    print(capitalize_first_char(sample4))
    print(capitalize_first_char(sample5))