def power_mod(base: int, exp: int, mod: int = None) -> int:
    if mod is not None and mod == 1:
        return 0
    if mod is None:
        if exp < 0:
            raise ValueError("Negative exponent requires modulus")
        return base ** exp
    if exp < 0:
        return pow(base, exp, mod)
    if exp == 0:
        return 1 % mod
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

if __name__ == '__main__':
    print(power_mod(2, 10, 1000))
    print(power_mod(3, 100, 97))
    print(power_mod(5, 0, 123))