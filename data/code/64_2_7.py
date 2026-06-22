def power(base, exponent):
    if isinstance(base, (int, float)) and isinstance(exponent, (int, float)):
        if exponent == int(exponent):
            exp_int = int(exponent)
            if exp_int < 0:
                base = 1 / base
                exp_int = -exp_int
            result = 1
            current = base
            while exp_int > 0:
                if exp_int % 2 == 1:
                    result *= current
                current *= current
                exp_int //= 2
            return result
        else:
            import math
            if base < 0:
                raise ValueError("base is negative and exponent is not an integer")
            return math.exp(exponent * math.log(abs(base)) if base != 0 else -float('inf') if exponent > 0 else float('inf') if exponent < 0 else 1.0)
    raise TypeError("base and exponent must be int or float")

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 3))
    print(power(2, -2))
    print(power(4, 0.5))
    print(power(5, 0))
    print(power(0.5, 3))
    print(power(2.5, 2))
    print(power(-2, 3))
    print(power(10, 1))
    print(power(7, -1))