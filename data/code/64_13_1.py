def mod_pow(base, exp, mod):
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

def pow_large(base, exp):
    return pow(base, exp)

if __name__ == '__main__':
    print(pow_large(2, 10))
    print(mod_pow(2, 10, 1000))
    print(pow_large(123456789, 987654321))
    print(mod_pow(123456789, 987654321, 1000000007))
    print(pow_large(0, 5))
    print(mod_pow(0, 5, 100))
    print(pow_large(1, 1000))
    print(mod_pow(1, 1000, 100))
    print(pow_large(2, 0))
    print(mod_pow(2, 0, 100))