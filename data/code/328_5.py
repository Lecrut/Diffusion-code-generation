def char_lengths_generator(input_string):
    for char in input_string:
        yield len(char)
if __name__ == '__main__':
    test_string = "hello world"
    generator = char_lengths_generator(test_string)
    result_list = list(generator)
    print(result_list)