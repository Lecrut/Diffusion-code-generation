def print_unicode_chars(s):
    for char in s:
        print(f"{char}: {ord(char)}")

if __name__ == '__main__':
    sample_string = "hello"
    print_unicode_chars(sample_string)