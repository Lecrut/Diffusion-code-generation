def digital_root(n):
    n = abs(n)
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    return n % 9

if __name__ == '__main__':
    values = [0, 18, 189, -12345]
    for v in values:
        print(digital_root(v))