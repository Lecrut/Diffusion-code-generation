def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n != 0:
        digit = n % 10
        if reversed_num > (2**31 - 1) // 10 or (reversed_num == (2**31 - 1) // 10 and digit > 7):
            return 0
        reversed_num = reversed_num * 10 + digit
        n //= 10
    result = sign * reversed_num
    if result < -(2**31) or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1534236469))
    print(reverse_integer(14638912513))