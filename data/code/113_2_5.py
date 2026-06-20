def validate_numbers(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers")

def high_precision_subtraction(x, y):
    validate_numbers(x, y)
    return x - y

if __name__ == '__main__':
    value1 = 23.4567890123456789
    value2 = 12.3456789012345678
    result = high_precision_subtraction(value1, value2)
    print(result)