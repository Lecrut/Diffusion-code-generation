def reverse_integer(n: int) -> int:
    if n == 0:
        return 0
    negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    if negative:
        reversed_num = -reversed_num
    return reversed_num

if __name__ == '__main__':
    test_values = [123, -456, 0, 907, -8001, 1534236469]
    for value in test_values:
        print(reverse_integer(value))