def is_valid_string(input_value):
    return isinstance(input_value, str)

def reverse_string(input_string):
    if not is_valid_string(input_string):
        raise ValueError("Input must be a string")
    reversed_chars = []
    for char in input_string:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_values = [
        "hello",
        "world",
        "Python3.8",
        "!@#$%",
        "12345"
    ]
    for value in sample_values:
        try:
            print(reverse_string(value))
        except ValueError as e:
            print(e)