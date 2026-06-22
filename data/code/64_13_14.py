import math

def power_mod(base: int, exp: int, mod: int) -> int:
    if mod == 1:
        return 0
    if exp < 0:
        base = pow(base, -1, mod)
        exp = -exp
    if base == 0:
        return 0 if exp > 0 else 1
    if exp == 0:
        return 1
    return pow(base, exp, mod)

if __name__ == '__main__':
    result = power_mod(2, 10, 1000)
    print(result)