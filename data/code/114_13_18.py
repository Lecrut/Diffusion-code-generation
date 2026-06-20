def validate_inputs(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")

def multiply_values(a, b):
    validate_inputs(a, b)
    return a * b

if __name__ == '__main__':
    result = multiply_values(5, 10)
    print(result)