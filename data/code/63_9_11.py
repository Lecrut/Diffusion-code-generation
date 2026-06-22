def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_str = str(abs(n))[::-1]
    reversed_num = int(reversed_str) * sign
    if reversed_num > 2**31 - 1 or reversed_num < -2**31:
        return 0
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))