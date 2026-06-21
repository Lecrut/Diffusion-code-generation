def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string

def separate_characters(input_string):
    validated_string = validate_input(input_string)
    return ','.join(validated_string)

if __name__ == '__main__':
    sample_string = "HelloWorld"
    print(separate_characters(sample_string))