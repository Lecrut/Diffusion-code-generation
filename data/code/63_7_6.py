def reverse_integer(n: int) -> int:
    if n < 0:
        sign = -1
        x = -n
    else:
        sign = 1
        x = n
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return sign * reversed_num

if __name__ == '__main__':
    test_values = [123, -456, 0, 120, -987654321]
    for val in test_values:
        print(val, reverse_integer(val))