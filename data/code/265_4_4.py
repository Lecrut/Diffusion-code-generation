def odd_ascii_chars(input_string):
    for char in input_string:
        if ord(char) % 2 != 0:
            yield char
if __name__ == '__main__':
    test_string = "Hello World!"
    result_generator = odd_ascii_chars(test_string)
    output_list = list(result_generator)
    print(output_list)