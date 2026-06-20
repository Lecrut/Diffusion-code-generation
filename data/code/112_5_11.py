def validate_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    return a, b

def sum_numbers(a, b):
    return a + b

if __name__ == '__main__':
    num1, num2 = validate_numbers(10, 5)
    result = sum_numbers(num1, num2)
    print(result)