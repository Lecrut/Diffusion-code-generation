def print_unicode_chars(string):
    for char in string:
        print(ord(char))

if __name__ == '__main__':
    sample_string = "hello"
    print_unicode_chars(sample_string)