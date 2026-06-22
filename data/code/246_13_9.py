def validate_decimals(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return True

def add_decimals(a, b):
    validate_decimals(a, b)
    return a + b

if __name__ == '__main__':
    value1 = 4.25
    value2 = 3.75
    result = add_decimals(value1, value2)
    print(result)