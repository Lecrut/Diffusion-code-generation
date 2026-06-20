def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")

def add(num1, num2):
    validate_integer(num1)
    validate_integer(num2)
    return num1 + num2

def subtract(num1, num2):
    validate_integer(num1)
    validate_integer(num2)
    return num1 - num2

if __name__ == '__main__':
    result_add = add(15, 27)
    print(result_add)
    result_subtract = subtract(30, 10)
    print(result_subtract)