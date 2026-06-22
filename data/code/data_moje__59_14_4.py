def digital_root_sum(n):
    n = abs(n)
    if n == 0:
        return 0
    while n > 9:
        s = 0
        while n:
            s += n & 15
            n >>= 4
        n = s
    return n

if __name__ == '__main__':
    print(digital_root_sum(0))
    print(digital_root_sum(12345))
    print(digital_root_sum(-9876))
    print(digital_root_sum(10))
    print(digital_root_sum(999))