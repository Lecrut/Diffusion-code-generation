def print_chars(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    for char in input_string:
        print(char)

if __name__ == '__main__':
    try:
        sample_string = "Hello, World!"
        print_chars(sample_string)
    except ValueError as e:
        print(e)