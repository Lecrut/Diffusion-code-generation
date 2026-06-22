def power(base, exponent):
    if exponent == 0:
        return 1
    result = 1
    current_product = base
    exp = exponent
    while exp > 0:
        if exp & 1:
            result *= current_product
        current_product *= current_product
        exp >>= 1
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(5, 3))