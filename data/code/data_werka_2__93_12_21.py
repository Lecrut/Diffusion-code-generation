def validate_boolean(value):
    if value is not False and value is not True:
        raise ValueError("Input must be a boolean")
    return value

def check_false_pair(a, b):
    validated_a = validate_boolean(a)
    validated_b = validate_boolean(b)
    return validated_a is False and validated_b is False

if __name__ == '__main__':
    A = False
    B = False
    result = check_false_pair(A, B)
    print(result)