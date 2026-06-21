def split_string_by_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string.split()

if __name__ == '__main__':
    sample_string = 'Hello World from Python'
    result = split_string_by_spaces(sample_string)
    print(result)