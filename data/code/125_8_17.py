def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")

def add(a, b):
    validate_integer(a)
    validate_integer(b)
    return a + b

def subtract(a, b):
    validate_integer(a)
    validate_integer(b)
    return a - b

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")