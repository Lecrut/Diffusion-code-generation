def has_special_chars(s):
    import string
    special_chars = set(string.punctuation)
    return any(c in special_chars for c in s)

if __name__ == '__main__':
    sample_strings = ["Hello World", "Hello, World!", "no_special_chars"]
    for s in sample_strings:
        print(has_special_chars(s))
    print(has_special_chars("test@#$"))