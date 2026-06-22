def contains_only_digits_and_spaces(input_string):
    return input_string.isdigit() or all(char == ' ' for char in input_string)

if __name__ == '__main__':
    sample_string = "12345 67890"
    result = contains_only_digits_and_spaces(sample_string)
    print(result)