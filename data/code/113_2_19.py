def subtract_floats(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both inputs must be floating-point numbers")
    return a - b

if __name__ == '__main__':
    result = subtract_floats(3.141592653589793, 2.718281828459045)
    print(result)