def validate_numbers(a, b):
    if not all(isinstance(num, (int, float)) for num in [a, b]):
        raise ValueError("Both inputs must be numbers")

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