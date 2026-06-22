def power_of_base(base: float, exponent: float) -> float:
    if base == 0 and exponent <= 0:
        raise ValueError("0 raised to a non-positive power is undefined.")
    if base < 0 and exponent != int(exponent):
        raise ValueError("Cannot raise a negative base to a fractional exponent in real domain.")
    return float(base ** exponent)

if __name__ == '__main__':
    result = power_of_base(2.0, 3.0)
    print(result)
    result = power_of_base(9.0, 0.5)
    print(result)
    result = power_of_base(-2.0, 2.0)
    print(result)
    result = power_of_base(2.0, 0.1)
    print(result)