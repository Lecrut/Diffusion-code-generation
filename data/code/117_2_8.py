def validate_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Both inputs must be numbers")

def subtract_numbers(a: float, b: float) -> float:
    validate_number(a)
    validate_number(b)
    return a - b

if __name__ == '__main__':
    result = subtract_numbers(10.5, 3.2)
    print(result)