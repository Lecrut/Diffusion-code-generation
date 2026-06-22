def validate_numbers(a, b):
    if not isinstance(a, (int, float)):
        raise ValueError("First argument must be an integer or float.")
    if not isinstance(b, (int, float)):
        raise ValueError("Second argument must be an integer or float.")

def sum_two_numbers(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 42
    num2 = 78
    try:
        result = sum_two_numbers(num1, num2)
        print(result)
    except ValueError as e:
        print(e)