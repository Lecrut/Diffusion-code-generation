def multiply(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both arguments must be floats")
    return a * b

if __name__ == '__main__':
    result = multiply(3.141592653589793, 2.718281828459045)
    print(result)