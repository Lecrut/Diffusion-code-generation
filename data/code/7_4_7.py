def first_special_char(s):
    import string
    special_chars = set(string.punctuation)
    for char in s:
        if char in special_chars:
            return char
    return None

if __name__ == '__main__':
    print(first_special_char("hello world"))
    print(first_special_char("hello, world!"))
    print(first_special_char("no special here"))
    print(first_special_char("!!!"))