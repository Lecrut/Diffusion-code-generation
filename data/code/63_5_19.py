def reverse_integer(n: int) -> int:
    if n == 0:
        return 0

    negative = n < 0
    num = abs(n)
    reversed_num = 0

    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10

    if negative:
        reversed_num = -reversed_num

    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    if not (INT_MIN <= reversed_num <= INT_MAX):
        return 0

    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))