def capitalize_first_letter(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_string = "hello world"
    print(capitalize_first_letter(test_string))