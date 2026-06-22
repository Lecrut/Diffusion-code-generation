def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def repeat_string(input_string):
    return input_string * 4

if __name__ == '__main__':
    sample_value = "hello"
    validate_input(sample_value)
    result = repeat_string(sample_value)
    print(result)