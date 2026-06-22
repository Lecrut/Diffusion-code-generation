import sys

def reverse_integer(n: int) -> int:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    negative = n < 0
    if negative:
        n = -n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        reversed_num = reversed_num * 10 + digit
    if negative:
        reversed_num = -reversed_num
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0
    return reversed_num
if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))