def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    return sign * reversed_n

if __name__ == '__main__':
    sample_values = [123, -456, 7890, 120, 0]
    for val in sample_values:
        print(reverse_integer(val))