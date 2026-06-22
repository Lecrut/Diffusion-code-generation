def reverse_integer(n):
    negative = n < 0
    n = abs(n)
    reversed_val = 0
    while n > 0:
        digit = n % 10
        reversed_val = reversed_val * 10 + digit
        n //= 10
    if negative:
        return -reversed_val
    return reversed_val

if __name__ == '__main__':
    test_values = [123, -456, 120, 0, 987654321]
    for val in test_values:
        print(reverse_integer(val))