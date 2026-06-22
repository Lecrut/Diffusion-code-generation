def digital_root_like_sum(n):
    n = abs(n)
    if n == 0:
        return 0
    total = 0
    while n > 0:
        total += n & 1
        n >>= 1
    return total

if __name__ == '__main__':
    print(digital_root_like_sum(0))
    print(digital_root_like_sum(5))
    print(digital_root_like_sum(-7))
    print(digital_root_like_sum(10))
    print(digital_root_like_sum(255))