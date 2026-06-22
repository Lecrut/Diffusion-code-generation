def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if exponent == 0:
        return 1.0
    if exponent < 0:
        base = 1.0 / base
        exponent = -exponent
    result = 1.0
    for _ in range(exponent):
        try:
            result *= base
            if result > 1e308:
                raise OverflowError("Result exceeds maximum floating point value")
        except OverflowError:
            raise
    return result

if __name__ == "__main__":
    val1 = power(2.5, 3)
    print(val1)
    val2 = power(10.0, -2)
    print(val2)
    try:
        val3 = power(10.0, 500)
        print(val3)
    except OverflowError:
        print("Overflow caught as expected")