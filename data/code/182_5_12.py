def char_generator(input_string):
    for char in input_string:
        yield char

if __name__ == '__main__':
    SAMPLE_STRING = "Hello World"
    generator = char_generator(SAMPLE_STRING)
    result_list = list(generator)
    print(result_list)