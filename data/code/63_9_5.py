def reverse_digits(n):
    negative = n < 0
    num = abs(n)
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    if negative:
        reversed_num = -reversed_num
    return reversed_num

if __name__ == '__main__':
    test_cases = [123, -456, 120, 0, 78900, -101]
    for case in test_cases:
        result = reverse_digits(case)
        print(result)