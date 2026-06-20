def validate_numbers(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise ValueError("Both inputs must be numbers")

def add_numbers(a, b):
    validate_numbers(a, b)
    return a + b

def subtract_numbers(a, b):
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    num1 = 25
    num2 = 10
    print("Addition Result:", add_numbers(num1, num2))
    print("Subtraction Result:", subtract_numbers(num1, num2))