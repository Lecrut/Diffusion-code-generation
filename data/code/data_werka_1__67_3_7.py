def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers (int or float).")

def sum_generator(a: float, b: float) -> float:
    validate_numbers(a, b)
    yield a + b

if __name__ == '__main__':
    num1 = 7.0
    num2 = 3.5
    result = next(sum_generator(num1, num2))
    print(result)