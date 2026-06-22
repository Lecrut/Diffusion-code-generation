def power_with_mod(base, exp, mod=None):
    if mod is not None:
        return pow(base, exp, mod)
    return pow(base, exp)

if __name__ == '__main__':
    result = power_with_mod(2, 10, 1000)
    print(result)
    
    result2 = power_with_mod(3, 4)
    print(result2)