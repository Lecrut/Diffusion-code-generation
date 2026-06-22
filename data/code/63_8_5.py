def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    rev = 0
    while n_abs > 0:
        digit = n_abs % 10
        n_abs = n_abs // 10
        if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and digit > 7):
            return 0
        rev = rev * 10 + digit
    return sign * rev

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))
    print(reverse_integer(1000000003))