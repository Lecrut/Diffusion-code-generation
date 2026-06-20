def is_zero(value: float, epsilon: float = 1e-9) -> bool:
    return abs(value) < epsilon

if __name__ == '__main__':
    print(is_zero(0.0))
    print(is_zero(1e-10))
    print(is_zero(1e-8))