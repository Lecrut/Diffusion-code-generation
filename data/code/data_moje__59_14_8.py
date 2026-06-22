def digital_root_sum(n):
    n = abs(n)
    if n == 0:
        return 0
    total = 0
    while n > 0:
        digit = n & 1
        total += digit
        n >>= 1
    return total

if __name__ == '__main__':
    print(digital_root_sum(123))
    print(digital_root_sum(0))
    print(digital_root_sum(-456))
    print(digital_root_sum(999999999))