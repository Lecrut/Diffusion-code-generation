def compute_digit_sum(n: int) -> int:
    abs_n = n if n >= 0 else -n
    total = 0
    while abs_n > 0:
        digit = abs_n & 15
        if digit > 9:
            digit = (digit & 7) + (digit >> 3) * 4
        total += digit
        abs_n >>= 4
        if total > 9:
            while total > 9:
                total = (total & 15) + (total >> 4)
    return total

if __name__ == '__main__':
    print(compute_digit_sum(0))
    print(compute_digit_sum(123456789))
    print(compute_digit_sum(-987654321))
    print(compute_digit_sum(999999999))
    print(compute_digit_sum(42))
    print(compute_digit_sum(-42))
    print(compute_digit_sum(100))