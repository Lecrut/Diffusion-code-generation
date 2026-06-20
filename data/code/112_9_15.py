def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numeric types.")

def add_numbers(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    result = add_numbers(3, 5)
    print(result)