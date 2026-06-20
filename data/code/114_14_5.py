def multiply(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers")
    return a * b

if __name__ == '__main__':
    result = multiply(4, 3)
    print(result)