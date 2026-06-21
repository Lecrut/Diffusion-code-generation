def separate_characters(input_string):
    if not isinstance(input_string, str) or not input_string:
        raise ValueError("Input must be a non-empty string.")
    
    return '-'.join([char for char in input_string])

if __name__ == '__main__':
    sample_string = "Hello World"
    result = separate_characters(sample_string)
    print(result)