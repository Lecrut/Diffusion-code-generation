def power(base: float, exponent: float) -> float:
    if isinstance(exponent, int):
        if exponent == 0:
            return 1.0
        if exponent < 0:
            base = 1.0 / base
            exponent = -exponent
        result = 1.0
        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2
        return result
    return base ** exponent

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3.5, 2))
    print(power(10, -2))
    print(power(0, 0))