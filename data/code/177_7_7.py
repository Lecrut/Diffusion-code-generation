def split_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string.split()

if __name__ == '__main__':
    sample_string = 'Python is awesome'
    try:
        result = split_string(sample_string)
        print(result)
    except ValueError as e:
        print(e)