def validate_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return True

def calculate_difference(a, b):
    if validate_numbers(a, b):
        return a - b

if __name__ == '__main__':
    num1 = 1234567890
    num2 = 987654321
    result = calculate_difference(num1, num2)
    print(result)