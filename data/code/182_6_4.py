def separate_chars_by_ord(s):
    return [ord(c) for c in s]

if __name__ == '__main__':
    sample_string = "hello"
    print(separate_chars_by_ord(sample_string))