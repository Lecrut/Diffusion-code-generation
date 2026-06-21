def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def separate_characters(input_string):
    validate_input(input_string)
    return ','.join(input_string)

if __name__ == '__main__':
    sample_string = "PythonProgramming"
    print(separate_characters(sample_string))