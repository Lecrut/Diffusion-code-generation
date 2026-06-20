def validate_floats(a, b, c):
    if not all(isinstance(i, float) for i in [a, b, c]):
        raise ValueError("All inputs must be of type float")

def sum_three_floats(a: float, b: float, c: float) -> float:
    validate_floats(a, b, c)
    return a + b + c

if __name__ == '__main__':
    result = sum_three_floats(1.1, 2.2, 3.3)
    print(result)