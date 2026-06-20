def multiply_decimals(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a * b

if __name__ == '__main__':
    result = multiply_decimals(0.1, 0.2)
    print(result)