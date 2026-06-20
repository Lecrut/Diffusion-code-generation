def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")

def calculate_difference(a, b):
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    value1 = 30
    value2 = 12
    result = calculate_difference(value1, value2)
    print(result)