def modular_power(base, exp, mod):
    return pow(base, exp, mod)

if __name__ == '__main__':
    result = modular_power(2, 10, 1000)
    print(result)