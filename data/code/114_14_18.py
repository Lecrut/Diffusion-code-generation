def validate_inputs(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")

def multiply_numbers(num1, num2):
    validate_inputs(num1, num2)
    return num1 * num2

if __name__ == '__main__':
    x = 7
    y = 3
    result = multiply_numbers(x, y)
    print(result)