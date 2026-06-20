from functools import mul

def validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a, b

def multiply(a, b):
    validated_a, validated_b = validate_numbers(a, b)
    return mul(validated_a, validated_b)

if __name__ == '__main__':
    result = multiply(4, 3)
    print(result)