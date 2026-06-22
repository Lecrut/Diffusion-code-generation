def power(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1.0
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Cannot raise zero to a negative power")
        result = 1.0
        for _ in range(-exponent):
            result /= base
            if not (result == result and result != float('inf')):
                raise OverflowError("Result overflowed")
        return result
    result = 1.0
    for _ in range(exponent):
        result *= base
        if not (result == result and result != float('inf')):
            raise OverflowError("Result overflowed")
    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(5.0, -2))
    try:
        print(power(1000000.0, 1000))
    except OverflowError:
        print("Caught OverflowError")
    print(power(0.0, 5))
    print(power(0.0, 0))
    try:
        print(power(0.0, -1))
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")