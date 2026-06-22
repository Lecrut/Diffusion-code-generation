def reverse_digits(n):
    if n == 0:
        return 0
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_str = str(abs_n).rstrip('0')[::-1]
    if reversed_str == '':
        return 0
    result = sign * int(reversed_str)
    max_val = 2**31 - 1
    min_val = -(2**31)
    if result < min_val or result > max_val:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_digits(123))
    print(reverse_digits(-123))
    print(reverse_digits(1200))
    print(reverse_digits(0))
    print(reverse_digits(1000000003))