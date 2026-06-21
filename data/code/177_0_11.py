def split_string_by_spaces(input_str):
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")
    
    return input_str.split()

if __name__ == '__main__':
    sample_string = "Hello World This is a test"
    print(split_string_by_spaces(sample_string))