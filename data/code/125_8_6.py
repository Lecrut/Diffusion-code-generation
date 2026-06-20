def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Value must be an integer")

def add(a, b):
    validate_integer(a)
    validate_integer(b)
    return a + b

def subtract(a, b):
    validate_integer(a)
    validate_integer(b)
    return a - b

if __name__ == '__main__':
    try:
        num1 = 5
        num2 = 3
        result_add = add(num1, num2)
        result_subtract = subtract(num1, num2)
        print(f"Addition: {result_add}")
        print(f"Subtraction: {result_subtract}")
    except ValueError as e:
        print(e)