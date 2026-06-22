def validate_boolean_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean type")
    return value

def get_bitwise_opposite(value):
    validated = validate_boolean_input(value)
    inverted = ~int(validated)
    result = inverted & 1
    return bool(result)

if __name__ == '__main__':
    print(get_bitwise_opposite(True))
    print(get_bitwise_opposite(False))