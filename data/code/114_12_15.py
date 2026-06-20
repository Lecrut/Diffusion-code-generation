def validate_numbers(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both inputs must be floating-point numbers.")

def multiply_numbers(a, b):
    validate_numbers(a, b)
    return a * b

if __name__ == '__main__':
    num1 = 3.141592653589793
    num2 = 2.718281828459045
    result = multiply_numbers(num1, num2)
    print(result)