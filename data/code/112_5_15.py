def validate_input(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Inputs must be numbers")

def sum_numbers(a, b):
    validate_input(a, b)
    return a + b

if __name__ == '__main__':
    result = sum_numbers(10, 5)
    print(result)