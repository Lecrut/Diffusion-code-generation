def capitalize_first_letter(s: str) -> str:
    return s[:1].upper() + s[1:] if s else s

if __name__ == '__main__':
    sample_string = "hello world"
    result = capitalize_first_letter(sample_string)
    print(result)
    print(capitalize_first_letter(""))
    print(capitalize_first_letter("123abc"))