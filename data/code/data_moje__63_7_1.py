def reverse_integer(n: int) -> int:
    negative = n < 0
    if negative:
        n = -n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return -reversed_num if negative else reversed_num

if __name__ == '__main__':
    test_value_1 = 12345
    test_value_2 = -5678
    test_value_3 = 0
    test_value_4 = 100
    print(reverse_integer(test_value_1))
    print(reverse_integer(test_value_2))
    print(reverse_integer(test_value_3))
    print(reverse_integer(test_value_4))