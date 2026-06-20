def validate_input(a, b, c):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise ValueError("All inputs must be floats or integers.")
    return True

def sum_floats(a: float, b: float, c: float) -> float:
    validate_input(a, b, c)
    return a + b + c

if __name__ == '__main__':
    result = sum_floats(1.1, 2.2, 3.3)
    print(result)