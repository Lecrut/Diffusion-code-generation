def digital_root(n):
    n = abs(n)
    if n == 0:
        return 0
    res = n % 9
    if res == 0:
        return 9
    return res

if __name__ == '__main__':
    print(digital_root(0))
    print(digital_root(18))
    print(digital_root(-19))
    print(digital_root(100))
    print(digital_root(1))
    print(digital_root(999999999))
    print(digital_root(-123456))
    print(digital_root(10))