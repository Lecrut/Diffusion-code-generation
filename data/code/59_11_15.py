def digit_sum(n):
    if n < 0:
        n = -n
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
if __name__ == '__main__':
    test_values = [0, 5, 123, 999999999999999999, 10 ** 18 - 1]
    for val in test_values:
        result = digit_sum(val)
        print(result)