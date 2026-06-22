def validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a, b

def add_numbers(a, b):
    a, b = validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    result = add_numbers(3, 5)
    print(result)