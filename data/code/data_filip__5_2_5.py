def capitalize_first_letter(text):
    if not text:
        return text
    if text[0].isalpha():
        return text[0].upper() + text[1:]
    for i, char in enumerate(text):
        if char.isalpha():
            return text[:i] + char.upper() + text[i + 1:]
    return text

if __name__ == '__main__':
    print(capitalize_first_letter("hello world"))
    print(capitalize_first_letter("python is great"))
    print(capitalize_first_letter("  leading spaces"))
    print(capitalize_first_letter("already Capitalized"))
    print(capitalize_first_letter(""))