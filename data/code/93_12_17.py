def validate_boolean(value):
    if value is not False and value is not True:
        raise ValueError("Input must be a boolean")
    return value

def both_are_false(a, b):
    validated_a = validate_boolean(a)
    validated_b = validate_boolean(b)
    return not validated_a and not validated_b

if __name__ == '__main__':
    A = False
    B = False
    result = both_are_false(A, B)
    print(result)
    A = True
    B = False
    result = both_are_false(A, B)
    print(result)