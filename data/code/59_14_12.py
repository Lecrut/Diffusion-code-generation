def compute_digit_sum(n):
    n = n if n >= 0 else -n
    if n == 0:
        return 0
    total = 0
    while n > 0:
        total += n & 15
        n >>= 4
        if n == 0:
            break
    if total > 9:
        total = compute_digit_sum(total)
    return total

if __name__ == '__main__':
    print(compute_digit_sum(12345))
    print(compute_digit_sum(-9876))
    print(compute_digit_sum(0))
    print(compute_digit_sum(999))
    print(compute_digit_sum(10))