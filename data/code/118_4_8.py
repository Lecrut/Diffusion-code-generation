from functools import mul

def validate_arguments(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a, b

def multiply(a, b):
    validated_args = validate_arguments(a, b)
    return mul(*validated_args)

if __name__ == '__main__':
    print(multiply(4, 3))