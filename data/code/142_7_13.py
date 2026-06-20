def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError('Input must be a boolean value')

def xnor(a: bool, b: bool) -> bool:
    validate_boolean(a)
    validate_boolean(b)
    return not a ^ b
if __name__ == '__main__':
    result1 = xnor(True, True)
    print(result1)
    result2 = xnor(False, False)
    print(result2)
    result3 = xnor(True, False)
    print(result3)
    result4 = xnor(False, True)
    print(result4)