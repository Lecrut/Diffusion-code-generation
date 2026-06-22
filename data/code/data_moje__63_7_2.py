def reverse_integer(n: int) -> int:
    negative = n < 0
    if negative:
        n = -n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    if negative:
        reversed_num = -reversed_num
    if reversed_num > 2**31 - 1 or reversed_num < -2**31:
        return 0
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1534236469))