def has_special_chars(text):
    return any(not char.isalnum() and not char.isspace() for char in text)

if __name__ == '__main__':
    print(has_special_chars("hello world"))
    print(has_special_chars("hello@world!"))
    print(has_special_chars("12345"))
    print(has_special_chars(""))