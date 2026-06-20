def validate_numbers(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise ValueError("Both inputs must be numbers")

def multiply(num1, num2):
    validate_numbers(num1, num2)
    return num1 * num2

if __name__ == '__main__':
    result = multiply(5, 10)
    print(result)
    result2 = multiply(3.5, 2)
    print(result2)