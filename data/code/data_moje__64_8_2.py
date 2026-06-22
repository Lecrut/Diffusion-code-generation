def compute_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an int or float")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an int or float")
    if exponent < 0 and base < 0:
        raise ValueError("Negative exponent with negative base is not allowed")
    if exponent < 0 and base == 0:
        raise ValueError("Zero base with negative exponent is undefined")
    
    result = 1
    exp = int(exponent) if exponent == int(exponent) else exponent
    
    if isinstance(exp, int):
        negative = exp < 0
        exp = abs(exp)
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        if negative:
            return 1.0 / result
        return result
    else:
        return base ** exponent

if __name__ == '__main__':
    print(compute_power(2, 10))
    print(compute_power(3, 3))
    print(compute_power(5, 0))
    print(compute_power(2, -2))
    print(compute_power(-2, 3))