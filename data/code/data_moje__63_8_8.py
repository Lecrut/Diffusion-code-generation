def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        if reversed_num > 2147483647:
            return 0
        n //= 10
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1534236469))