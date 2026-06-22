def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    reversed_str = str(n_abs)[::-1]
    reversed_int = int(reversed_str) * sign
    if reversed_int < -2**31 or reversed_int > 2**31 - 1:
        return 0
    return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))