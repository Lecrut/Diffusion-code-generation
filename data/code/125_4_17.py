def validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a, b

def add_numbers(a, b):
    a, b = validate_numbers(a, b)
    return a + b

def subtract_numbers(a, b):
    a, b = validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    num1 = 25
    num2 = 10
    print("Addition Result:", add_numbers(num1, num2))
    print("Subtraction Result:", subtract_numbers(num1, num2))