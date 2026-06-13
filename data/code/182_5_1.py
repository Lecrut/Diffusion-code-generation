def char_generator(input_string):
    for char in input_string:
        yield char
if __name__ == '__main__':
    sample_string = "Hello World"
    generator = char_generator(sample_string)
    result = list(generator)
    print(result)