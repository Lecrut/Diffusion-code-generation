def digital_root(n):
    n = abs(n)
    if n == 0:
        return 0
    result = 1 + (n - 1) % 9
    return result

if __name__ == '__main__':
    print(digital_root(38))
    print(digital_root(0))
    print(digital_root(-12345))
    print(digital_root(10))