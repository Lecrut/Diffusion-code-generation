def uppercase_char_generator(input_string):
    for char in input_string:
        yield char.upper()
if __name__ == '__main__':
    test_string = "hello world"
    generator = uppercase_char_generator(test_string)
    result_list = list(generator)
    print(result_list)