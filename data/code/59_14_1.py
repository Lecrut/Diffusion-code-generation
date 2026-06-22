def digital_root_sum(n):
    n = abs(n)
    while n >= 10:
        total = 0
        while n > 0:
            total += n & 15
            n >>= 4
        n = total
    return n

if __name__ == '__main__':
    print(digital_root_sum(0))
    print(digital_root_sum(-456))
    print(digital_root_sum(9999))
    print(digital_root_sum(123456))