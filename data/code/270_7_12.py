def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

def remove_spaces(s):
    validate_input(s)
    return s.translate(str.maketrans('', '', ' '))

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    result = remove_spaces(sample_string)
    print(result)