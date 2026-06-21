def validate_input(input_string):
    if not isinstance(input_string, str) or ',' not in input_string:
        raise ValueError("Input must be a string containing names separated by commas.")
    return input_string

def strip_names(names_str):
    validated_names = validate_input(names_str)
    return [name.strip() for name in validated_names.split(',')]

if __name__ == '__main__':
    sample_names = " Alice, Bob , Charlie "
    print(strip_names(sample_names))