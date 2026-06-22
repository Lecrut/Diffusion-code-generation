def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
    return sign * reversed_n

if __name__ == '__main__':
    test_cases = [123, -456, 120, 0, 1534236469]
    for case in test_cases:
        result = reverse_integer(case)
        print(result)