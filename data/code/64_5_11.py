def power_with_mod(base, exp, mod=None):
    if mod is None:
        return base ** exp
    return pow(base, exp, mod)

if __name__ == '__main__':
    result = power_with_mod(2, 10, 1000)
    print(result)