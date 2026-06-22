def validate_boolean(input_value):
    if type(input_value) is not bool:
        raise ValueError("Input must be a boolean type")
    return True

def negate_boolean(value):
    validate_boolean(value)
    return not value

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)