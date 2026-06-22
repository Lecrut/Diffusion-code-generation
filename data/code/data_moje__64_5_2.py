def power(base, exp, mod=None):
    if mod is not None:
        return pow(base, exp, mod)
    else:
        return pow(base, exp)

if __name__ == '__main__':
    result = power(2, 10, 1000)
    print(result)