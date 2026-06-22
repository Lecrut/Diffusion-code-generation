def reverse_integer(x):
    if x == 0:
        return 0
    negative = x < 0
    x = abs(x)
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    if reversed_num > 2**31 - 1:
        return 0
    return -reversed_num if negative else reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))