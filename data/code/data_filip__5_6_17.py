def capitalize_first_char(text: str) -> str:
    if not text:
        return text
    first = text[0].upper()
    return first + text[1:]

if __name__ == '__main__':
    test_cases = ["hello", "HELLO", "h", "", "café", "Étoile", "123abc", "Ñoño"]
    for case in test_cases:
        print(capitalize_first_char(case))