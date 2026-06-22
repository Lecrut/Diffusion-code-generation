def reverse_integer(n):
    negative = n < 0
    n = abs(n)
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return -reversed_n if negative else reversed_n

if __name__ == '__main__':
    test_cases = [123, -456, 7890, 0, 100]
    for tc in test_cases:
        print(reverse_integer(tc))