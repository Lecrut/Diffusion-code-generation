def subtract_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a - b

if __name__ == '__main__':
    result = subtract_numbers(3.141592653589793, 2.718281828459045)
    print(result)