def power(base, exp):
    result = 1
    base = base % 1000000007
    if base == 0:
        return 0
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % 1000000007
        exp = exp >> 1
        base = (base * base) % 1000000007
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 7))
    print(power(5, 0))
    print(power(10, 3))