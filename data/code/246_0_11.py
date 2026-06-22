def add_numbers(a, b):
    return a + b

def validate_input(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValueError("Both inputs must be integers")
    if x < 0 or y < 0:
        raise ValueError("Inputs must be non-negative")

if __name__ == '__main__':
    num1 = 15
    num2 = 27
    validate_input(num1, num2)
    result = add_numbers(num1, num2)
    print(result)