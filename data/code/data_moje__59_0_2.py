def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    test_values = [123, 987654321, 5, 1000]
    for value in test_values:
        print(sum_of_digits(value))