def raise_power(base, exponent):
    if isinstance(base, int) and isinstance(exponent, int):
        if exponent < 0:
            return 1.0 / _int_pow(abs(base), abs(exponent)) if base != 0 else float('inf') if base > 0 else float('-inf')
        return _int_pow(base, exponent)
    return float(base) ** float(exponent)

def _int_pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    half = _int_pow(base, exp // 2)
    result = half * half
    if exp % 2 == 1:
        result *= base
    return result

if __name__ == '__main__':
    print(raise_power(2, 10))
    print(raise_power(3, -2))
    print(raise_power(2.5, 3))
    print(raise_power(5, 0))
    print(raise_power(-2, 3))