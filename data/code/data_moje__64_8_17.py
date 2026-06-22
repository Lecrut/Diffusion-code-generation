def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if exponent < 0 and base < 0:
        raise ValueError("Negative exponent with negative base is not allowed")
    
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(-base, -exponent) if base > 0 else 1 / power(abs(base), -exponent)
    
    result = 1
    current = base
    exp = exponent
    
    while exp > 0:
        if exp % 2 == 1:
            result *= current
        current *= current
        exp //= 2
    
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 3))
    print(power(5, 0))
    print(power(2, -3))