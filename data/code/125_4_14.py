def validate_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")

def add_integers(a, b):
    validate_numbers(a, b)
    return a + b

def subtract_integers(a, b):
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    num1 = 25
    num2 = 10
    print(add_integers(num1, num2))
    print(subtract_integers(num1, num2))