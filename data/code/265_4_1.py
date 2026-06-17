def char_generator(input_string):
    for char in input_string:
        if ord(char) % 2 != 0:
            yield char
if __name__ == '__main__':
    test_string = "Hello World!"
    result_generator = char_generator(test_string)
    output_list = list(result_generator)
    print(output_list)