def contains_only_digits_and_spaces(input_string):
    return input_string.isdigit() or input_string.isspace()
if __name__ == '__main__':
    sample_string = '1234567890'
    print(contains_only_digits_and_spaces(sample_string))
    sample_string = 'hello world'
    print(contains_only_digits_and_spaces(sample_string))
    sample_string = '123 hello world'
    print(contains_only_digits_and_spaces(sample_string))