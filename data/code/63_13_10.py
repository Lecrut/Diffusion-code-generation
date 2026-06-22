def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return sign * reversed_num

if __name__ == '__main__':
    test_values = [123, -456, 0, 9810, -7]
    for val in test_values:
        print(f"Original: {val}, Reversed: {reverse_integer(val)}")