def multiply(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a * b

if __name__ == '__main__':
    result = multiply(4, 3)
    print(result)