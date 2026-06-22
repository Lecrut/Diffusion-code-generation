def digit_sum(n):
    if n < 0:
        n = -n
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    sample_values = [12345, 0, 987654321098765432, 1000000000000000000]
    for val in sample_values:
        print(digit_sum(val))