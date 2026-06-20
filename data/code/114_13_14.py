def validate_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative")

def multiply_values(a, b):
    validate_inputs(a, b)
    return a * b

if __name__ == '__main__':
    result = multiply_values(4, 3)
    print(result)