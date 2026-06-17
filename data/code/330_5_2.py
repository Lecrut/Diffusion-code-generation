def uppercase_char_generator(input_string):
    for char in input_string:
        yield char.upper()
if __name__ == '__main__':
    sample_string = "this is a very long string for testing memory efficiency"
    uppercase_generator = uppercase_char_generator(sample_string)
    result_list = list(uppercase_generator)
    print(result_list)