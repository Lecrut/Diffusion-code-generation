def validate_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative.")

def add_numbers(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    result = add_numbers(num1, num2)
    print(result)