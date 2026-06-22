def digital_root_like_sum(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    total = 0
    while n > 0:
        digit = n & 15
        total += digit
        n >>= 4
        if n == 0 and digit != 0:
            break
        elif n == 0 and digit == 0:
            break
    return total
if __name__ == '__main__':
    print(digital_root_like_sum(123))
    print(digital_root_like_sum(-456))
    print(digital_root_like_sum(0))
    print(digital_root_like_sum(999))
    print(digital_root_like_sum(-1))