def validate_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a, b

def calculate_difference(a, b):
    return a - b

if __name__ == '__main__':
    num1, num2 = validate_numbers(123456789012345678901234567890, 987654321098765432109876543210)
    result = calculate_difference(num1, num2)
    print(result)