def validate_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return True

def multiply_values(a, b):
    validate_inputs(a, b)
    return a * b

if __name__ == '__main__':
    result = multiply_values(7, 8)
    print(result)