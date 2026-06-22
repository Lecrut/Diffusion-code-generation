def validate_numbers(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both inputs must be floating-point numbers.")
    return a, b

def add_floats(a: float, b: float) -> float:
    validated_a, validated_b = validate_numbers(a, b)
    return validated_a + validated_b

if __name__ == '__main__':
    result = add_floats(3.141592653589793, 2.718281828459045)
    print(result)