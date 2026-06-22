def contains_only_digits_and_spaces(input_string):
    return all(char.isdigit() or char.isspace() for char in input_string)

if __name__ == '__main__':
    sample_string = "123 456"
    result = contains_only_digits_and_spaces(sample_string)
    print(result)