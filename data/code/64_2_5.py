def power(base, exponent):
    if isinstance(base, (int, float)) and isinstance(exponent, (int, float)):
        if base == 0 and exponent <= 0:
            raise ValueError("0 cannot be raised to a non-positive power")
        if exponent == 0:
            return 1
        if exponent > 0:
            result = 1
            exp = abs(exponent)
            if exp == int(exp):
                exp_int = int(exp)
                b = base
                while exp_int > 0:
                    if exp_int % 2 == 1:
                        result *= b
                    b *= b
                    exp_int //= 2
            else:
                result = base ** exp
            return result if exponent >= 0 else 1 / result
        else:
            return 1 / power(base, -exponent)
    else:
        raise TypeError("Base and exponent must be numeric types")

if __name__ == '__main__':
    print(power(2, 3))
    print(power(2, -3))
    print(power(4, 0.5))
    print(power(10, 3))
    print(power(2.5, 3))