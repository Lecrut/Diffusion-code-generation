def is_zero(value: float, epsilon: float = 1e-9) -> bool:
    if not isinstance(value, (int, float)) or not isinstance(epsilon, (int, float)):
        raise ValueError("Both value and epsilon must be numbers")
    return abs(value) < epsilon

if __name__ == '__main__':
    print(is_zero(0.0))
    print(is_zero(1e-10))
    print(is_zero(1e-8))
    print(is_zero(-1e-09))
    print(is_zero(123.456, 1))