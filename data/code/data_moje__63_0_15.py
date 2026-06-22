def reverse_integer(n):
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_str = str(abs_n)[::-1]
    result = int(reversed_str) * sign
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))