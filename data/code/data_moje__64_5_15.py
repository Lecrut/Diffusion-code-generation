def pow_mod(base, exp, mod=None):
    if mod is None:
        return pow(base, exp)
    return pow(base, exp, mod)

if __name__ == '__main__':
    print(pow_mod(2, 10))
    print(pow_mod(3, 7, 13))
    print(pow_mod(5, 100, 7))