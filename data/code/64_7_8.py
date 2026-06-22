def calculate_power(base: float, exponent: float) -> float:
    if exponent == 0:
        return 1.0
    if base == 0:
        if exponent > 0:
            return 0.0
        raise ValueError("0 to the power of 0 or negative is undefined")
    if base < 0:
        if exponent == int(exponent):
            return pow(base, exponent)
        raise ValueError("Cannot compute fractional power of a negative base")
    import math
    return math.exp(exponent * math.log(base))

if __name__ == '__main__':
    result = calculate_power(2.0, 0.5)
    print(result)