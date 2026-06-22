def has_special_characters(s):
    return any(not c.isalnum() and not c.isspace() for c in s)

if __name__ == '__main__':
    print(has_special_characters("hello world"))
    print(has_special_characters("hello@world!"))
    print(has_special_characters("no specials here"))
    print(has_special_characters("!@#"))