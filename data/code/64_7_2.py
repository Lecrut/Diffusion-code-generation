def calculate_power(base: float, exponent: float) -> float:
    if base == 0 and exponent <= 0:
        raise ValueError("0 cannot be raised to a non-positive power")
    if base < 0 and exponent != int(exponent):
        raise ValueError("Cannot raise negative base to a fractional exponent in real numbers")
    return float(pow(base, exponent))

if __name__ == '__main__':
    print(calculate_power(2.0, 3.0))
    print(calculate_power(4.0, 0.5))
    print(calculate_power(2.0, -3.0))
    print(calculate_power(10.0, 1.5))