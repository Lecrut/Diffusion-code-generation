def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be integers or floats.")

def sum_two_numbers(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 25
    num2 = 30
    result = sum_two_numbers(num1, num2)
    print(result)