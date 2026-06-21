def non_whitespace_generator(input_string):
    for char in input_string:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    SAMPLE_INPUT = "Hello World"
    result = ''.join(non_whitespace_generator(SAMPLE_INPUT))
    print(result)