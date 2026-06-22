def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_abs = 0
    while abs_n > 0:
        digit = abs_n % 10
        reversed_abs = reversed_abs * 10 + digit
        abs_n //= 10
    return sign * reversed_abs

if __name__ == '__main__':
    sample_values = [123, -456, 0, 1200]
    for val in sample_values:
        result = reverse_integer(val)
        print(result)