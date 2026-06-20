def multiply_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a * b

if __name__ == '__main__':
    result = multiply_numbers(4, 3)
    print(result)