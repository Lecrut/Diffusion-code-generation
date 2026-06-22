import math

def power(base: float, exponent: int) -> float:
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if exponent < 0:
        return 1.0 / power(base, -exponent)
    result = 1.0
    for _ in range(exponent):
        result *= base
        if math.isinf(result):
            raise OverflowError("Result overflowed")
    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(3.0, 0))
    print(power(1.5, 5))
    print(power(2.0, -3))
    try:
        power(10.0, 308)
    except OverflowError as e:
        print(str(e))