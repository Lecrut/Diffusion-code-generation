def reverse_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return ''.join(reversed(input_string))

if __name__ == '__main__':
    SAMPLE_VALUES = [
        "hello",
        "world",
        "Python3.8",
        "!@#$%",
        "12345"
    ]
    
    for value in SAMPLE_VALUES:
        try:
            print(reverse_string(value))
        except ValueError as e:
            print(e)