ALLOWED_CHARS = '0123456789 '

def contains_only_digits_and_spaces(input_string):
    return all((char in ALLOWED_CHARS for char in input_string))
if __name__ == '__main__':
    sample_string = '12345 6789'
    print(contains_only_digits_and_spaces(sample_string))
    sample_string = 'abc123def456'
    print(contains_only_digits_and_spaces(sample_string))