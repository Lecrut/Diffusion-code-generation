def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Both inputs must be integers")

def multiply_two_numbers(a, b):
    validate_integer(a)
    validate_integer(b)
    return a * b

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = multiply_two_numbers(num1, num2)
    print(result)