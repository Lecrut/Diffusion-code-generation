def split_by_space(input_string):
    if not isinstance(input_string, str) or not input_string:
        raise ValueError("Input must be a non-empty string")
    return input_string.split(' ')

if __name__ == '__main__':
    test_string = "split this string by spaces"
    result = split_by_space(test_string)
    print(result)