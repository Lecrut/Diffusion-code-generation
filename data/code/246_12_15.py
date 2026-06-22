def validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return True

def add_numbers(a, b):
    if not validate_numbers(a, b):
        return None
    return a + b

if __name__ == '__main__':
    result = add_numbers(3, 5)
    print(result)