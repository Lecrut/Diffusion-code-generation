def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if exponent < 0:
        if base == 0:
            raise ValueError("Cannot raise zero to a negative power")
        base = 1.0 / base
        exponent = -exponent
    result = 1.0
    current_base = base
    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_base
            if abs(result) > 1.8e308 and result != float('inf'):
                raise OverflowError("Result too large")
        current_base *= current_base
        exponent //= 2
    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(3.0, -2))
    print(power(5.0, 0))
    print(power(-2.5, 3))
    print(power(1.1, 100))