def multiply(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a * b

if __name__ == '__main__':
    result = multiply(3, 4)
    print(result)