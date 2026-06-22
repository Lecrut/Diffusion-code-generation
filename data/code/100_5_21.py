def validate_and_gate(input_a, input_b):
    if not isinstance(input_a, bool) or not isinstance(input_b, bool):
        raise ValueError("Inputs must be boolean values")
    if input_a is True and input_b is True:
        return True
    return False

if __name__ == '__main__':
    result = validate_and_gate(True, False)
    print(result)