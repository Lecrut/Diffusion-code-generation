def power(base, exp):
    if exp < 0:
        base = 1 / base
        exp = -exp
    
    result = 1
    current = base
    
    while exp > 0:
        if exp % 2 == 1:
            result *= current
        current *= current
        exp //= 2
    
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 5))
    print(power(-2, 4))
    print(power(5, 0))