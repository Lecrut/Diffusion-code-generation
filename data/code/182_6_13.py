def separate_chars_by_ord(input_string):
    return [ord(c) for c in input_string]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = separate_chars_by_ord(sample_string)
    print(result)