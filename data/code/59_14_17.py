def digital_root(n):
    n = abs(n)
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    return n % 9

if __name__ == '__main__':
    print(digital_root(942))
    print(digital_root(-123))
    print(digital_root(0))
    print(digital_root(10))