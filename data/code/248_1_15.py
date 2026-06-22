def validate_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")

def add_two_numbers(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = add_two_numbers(num1, num2)
    print(result)