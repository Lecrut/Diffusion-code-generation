def validate_inputs(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be valid numbers.")

def multiply_numbers(a, b):
    return a * b

if __name__ == '__main__':
    num1 = 15
    num2 = 7
    validate_inputs(num1, num2)
    result = multiply_numbers(num1, num2)
    print(result)