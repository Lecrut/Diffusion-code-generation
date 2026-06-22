def contains_only_digits_and_spaces(input_string):
    for char in input_string:
        if not (char.isdigit() or char.isspace()):
            return False
    return True

if __name__ == '__main__':
    test_string = "12345 67890"
    result = contains_only_digits_and_spaces(test_string)
    print(result)