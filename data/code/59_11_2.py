def digit_sum(n):
    s = 0
    if n < 0:
        n = -n
    while n > 0:
        s += n % 10
        n //= 10
    return s

if __name__ == '__main__':
    sample_values = [0, 5, 123, 9876543210, 10**18]
    for value in sample_values:
        print(digit_sum(value))