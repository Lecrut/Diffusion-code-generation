def pow_mod(base, exp, mod):
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
    return base ** exp

if __name__ == '__main__':
    res1 = pow_mod(2, 10, 1000)
    print(res1)
    
    res2 = pow_large(2, 100)
    print(res2)