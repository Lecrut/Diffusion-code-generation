def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def check_difference(a, b):
    validate_numbers(a, b)
    return a != b

if __name__ == '__main__':
    value1 = 42.0
    value2 = 43.5
    result = check_difference(value1, value2)
    print(result)