def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")

def add_values(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    print(add_values(3, 5))
    print(add_values(-2, 7.5))