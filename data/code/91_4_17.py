def validate_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value

def invert_logic(flag):
    return not flag

def process_boolean_input(raw_input):
    validated = validate_input(raw_input)
    return invert_logic(validated)

if __name__ == '__main__':
    samples = [True, False]
    for sample in samples:
        result = process_boolean_input(sample)
        print(result)