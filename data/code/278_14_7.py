def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def print_chars(input_string):
    validate_input(input_string)
    for char in input_string:
        print(char)

if __name__ == '__main__':
    try:
        print_chars("Hello, World!")
    except ValueError as e:
        print(e)