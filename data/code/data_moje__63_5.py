def reverse_integer(n: int) -> int:
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    reversed_n *= sign
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if reversed_n > INT_MAX or reversed_n < INT_MIN:
        return 0
    return reversed_n

if __name__ == '__main__':
    result = reverse_integer(123)
    print(result)
    result2 = reverse_integer(-456)
    print(result2)
    result3 = reverse_integer(1200)
    print(result3)