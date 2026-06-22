def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return sign * reversed_num

if __name__ == '__main__':
    sample_value = -12345
    result = reverse_integer(sample_value)
    print(result)