def validate_input(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both inputs must be floating-point numbers.")
    return a, b

def multiply(a, b):
    return a * b

if __name__ == '__main__':
    value1 = 3.14159265358979323846
    value2 = 2.71828182845904523536
    validated_values = validate_input(value1, value2)
    result = multiply(*validated_values)
    print(result)