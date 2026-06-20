def has_special_chars(s):
    special = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')
    return any(c in special for c in s)

if __name__ == '__main__':
    print(has_special_chars("hello"))
    print(has_special_chars("hello!"))
    print(has_special_chars(""))
    print(has_special_chars("@#$"))