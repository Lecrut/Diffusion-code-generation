def ord_chars(s):
    return [ord(c) for c in s]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(ord_chars(sample_string))