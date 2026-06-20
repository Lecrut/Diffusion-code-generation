def validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Both inputs must be numbers")

def calculate_difference(num1: int | float, num2: int | float) -> int | float:
    validate_numeric(num1)
    validate_numeric(num2)
    return num1 - num2

if __name__ == '__main__':
    try:
        result = calculate_difference(100, 35)
        print(result)
    except TypeError as e:
        print(e)