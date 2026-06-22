def optimized_power(base, exponent):
    if isinstance(base, (int, float)) and isinstance(exponent, (int, float)):
        if base == 0 and exponent < 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        if isinstance(exponent, int) and exponent >= 0:
            result = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    result *= base
                base *= base
                exponent //= 2
            return result
        return base ** exponent
    raise TypeError("base and exponent must be numeric")

if __name__ == '__main__':
    print(optimized_power(2, 10))
    print(optimized_power(5.5, 3))
    print(optimized_power(2, -3))