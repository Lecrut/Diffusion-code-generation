def validate_float(value):
    if not isinstance(value, float):
        raise ValueError("All inputs must be of type float")

def sum_three_floats(a: float, b: float, c: float) -> float:
    validate_float(a)
    validate_float(b)
    validate_float(c)
    return a + b + c

if __name__ == '__main__':
    result = sum_three_floats(1.1, 2.2, 3.3)
    print(result)