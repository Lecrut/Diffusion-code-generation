def validate_numbers(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both inputs must be floating-point numbers")

def multiply(a, b):
    validate_numbers(a, b)
    return a * b

if __name__ == '__main__':
    result = multiply(3.141592653589793, 2.718281828459045)
    print(result)