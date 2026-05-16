def filter_string(input_string):
    for char in input_string:
        if not char.isspace():
            yield char
if __name__ == '__main__':
    test_string = "Hello World! \nThis is a test."
    result = list(filter_string(test_string))
    print(result)