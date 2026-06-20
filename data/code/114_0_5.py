def multiply_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a * b

if __name__ == '__main__':
    pi = 3.141592653589793
    e = 2.718281828459045
    result = multiply_numbers(pi, e)
    print(result)