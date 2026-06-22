def reverse_integer(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    return sign * reversed_n

if __name__ == '__main__':
    test_cases = [123, -456, 1200, 0, 7]
    for tc in test_cases:
        result = reverse_integer(tc)
        print(result)