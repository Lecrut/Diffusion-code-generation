def print_unicode_characters(input_string):
    for char in input_string:
        print(f"'{char}': {ord(char)}")

if __name__ == '__main__':
    sample_string = "hello"
    print_unicode_characters(sample_string)