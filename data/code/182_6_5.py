def separate_chars_by_ord(input_string):
    return [ord(char) for char in input_string]

if __name__ == '__main__':
    sample_string = "hello"
    print(separate_chars_by_ord(sample_string))