def split_by_space(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string.split()

if __name__ == '__main__':
    test_string = "split this string by spaces"
    result = split_by_space(test_string)
    print(result)