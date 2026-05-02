def filter_non_whitespace(input_string):
    for char in input_string:
        if not char.isspace():
            yield char
if __name__ == '__main__':
    test_string = "Hello World! \nThis is a test."
    result_generator = filter_non_whitespace(test_string)
    result_list = list(result_generator)
    print(result_list)