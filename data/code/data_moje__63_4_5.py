def reverse_integer(n):
    if n == 0:
        return 0
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev * sign

if __name__ == '__main__':
    val1 = 1234
    val2 = -5678
    val3 = 1200
    print(reverse_integer(val1))
    print(reverse_integer(val2))
    print(reverse_integer(val3))