def capitalize_sentence(text):
    if not text:
        return ""
    first_char = text[0]
    if first_char.isalpha():
        return text[0].upper() + text[1:]
    for i, char in enumerate(text):
        if char.isalpha():
            return text[:i] + char.upper() + text[i+1:]
    return text

if __name__ == '__main__':
    print(capitalize_sentence("hello world"))
    print(capitalize_sentence("123abc"))
    print(capitalize_sentence(""))
    print(capitalize_sentence("already Capitalized"))