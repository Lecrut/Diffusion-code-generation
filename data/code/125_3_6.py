def validate_numbers(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        raise ValueError("Both inputs must be integers.")
    if num1 < 0 or num2 < 0:
        raise ValueError("Both numbers must be non-negative.")

def add(a, b):
    validate_numbers(a, b)
    return a + b

def subtract(a, b):
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    result_add = add(15, 7)
    result_subtract = subtract(10, 4)
    print(f"Sum: {result_add}")
    print(f"Difference: {result_subtract}")