def reverse_integer(n: int) -> int:
    if n == 0:
        return 0
    negative = n < 0
    x = -n if negative else n
    result = 0
    while x != 0:
        digit = x % 10
        x //= 10
        result = result * 10 + digit
    if result > 2147483647:
        return 0
    return -result if negative else result

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-987))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))
    print(reverse_integer(-2147483648))