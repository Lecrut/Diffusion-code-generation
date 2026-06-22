def power_mod(base, exp, mod):
    if mod == 1:
        return 0
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
    print(power_mod(3, 100, 1000))
    print(power_mod(10, 10, 10000))
    print(power_mod(0, 100, 100))
    print(power_mod(5, 0, 1))