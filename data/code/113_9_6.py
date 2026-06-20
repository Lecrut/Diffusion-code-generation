def validate_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return a, b

def calculate_difference(a, b):
    return a - b

if __name__ == '__main__':
    num1 = 123456789012345678901234567890
    num2 = 987654321098765432109876543210
    validated_numbers = validate_numbers(num1, num2)
    result = calculate_difference(*validated_numbers)
    print(result)