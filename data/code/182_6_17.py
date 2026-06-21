def separate_chars_by_ord(s):
    return list(map(ord, s))

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = separate_chars_by_ord(sample_string)
    print(result)