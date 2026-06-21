def split_string(input_string):
    if not isinstance(input_string, str) or not input_string:
        raise ValueError("Input must be a non-empty string")
    
    return input_string.split()

if __name__ == '__main__':
    sample_string = 'Python is awesome'
    try:
        result = split_string(sample_string)
        print(result)
    except ValueError as e:
        print(e)