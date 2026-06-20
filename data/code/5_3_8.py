def capitalize_first_alphanumeric(text):
    if not text:
        return text
    for i, char in enumerate(text):
        if char.isalnum():
            return text[:i] + char.upper() + text[i + 1:]
    return text

if __name__ == '__main__':
    print(capitalize_first_alphanumeric("123abc"))
    print(capitalize_first_alphanumeric("hello world"))
    print(capitalize_first_alphanumeric("   xyz"))
    print(capitalize_first_alphanumeric("   456def"))
    print(capitalize_first_alphanumeric(""))