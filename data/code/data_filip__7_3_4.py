def has_special_chars(s):
    return any(not c.isalnum() and not c.isspace() for c in s)

if __name__ == '__main__':
    sample1 = "Hello World 123"
    sample2 = "Hello@World#123!"
    sample3 = "JustNumbers123"
    print(has_special_chars(sample1))
    print(has_special_chars(sample2))
    print(has_special_chars(sample3))