def char_length_generator(input_string):
    for char in input_string:
        yield len(char)
if __name__ == '__main__':
    test_string = "hello world"
    generator = char_length_generator(test_string)
    results = list(generator)
    print(results)