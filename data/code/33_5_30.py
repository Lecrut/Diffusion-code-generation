def non_whitespace_characters(input_string):
    for char in input_string:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    result = ''.join(non_whitespace_characters(sample_string))
    print(result)