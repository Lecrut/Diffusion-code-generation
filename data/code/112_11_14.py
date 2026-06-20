def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")

def add_two_numbers(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    result = add_two_numbers(3.5, 2.1)
    print(result)