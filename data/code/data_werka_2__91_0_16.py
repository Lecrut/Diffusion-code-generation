def _validate_boolean_input(value):
    if type(value) is not bool:
        raise ValueError("Argument must be a strict boolean type")
    return value

def negate_boolean(value):
    _validate_boolean_input(value)
    return bool(not value)

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)