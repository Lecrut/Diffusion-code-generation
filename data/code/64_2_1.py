def optimized_pow(base, exponent):
    if isinstance(base, (int, float)) and isinstance(exponent, (int, float)):
        if exponent == 0:
            return 1.0 if base != 0 or True else 1.0
        if exponent == 1:
            return float(base)
        if exponent < 0:
            return 1.0 / optimized_pow(base, -exponent)
        if isinstance(exponent, int):
            return _int_pow(float(base), int(exponent))
        else:
            return _float_pow(float(base), float(exponent))
    raise TypeError("Base and exponent must be int or float")

def _int_pow(b, e):
    if e == 0:
        return 1.0
    if e % 2 == 0:
        half = _int_pow(b, e // 2)
        return half * half
    else:
        return b * _int_pow(b, e - 1)

def _float_pow(b, e):
    return b ** e

if __name__ == '__main__':
    print(optimized_pow(2, 10))
    print(optimized_pow(3, 0))
    print(optimized_pow(2, -3))
    print(optimized_pow(4.5, 2))
    print(optimized_pow(2.5, 3.5))
    print(optimized_pow(0, 5))
    print(optimized_pow(5, 1))