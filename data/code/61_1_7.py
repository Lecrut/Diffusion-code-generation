def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** 0.5) + 1
    divisor = 3
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, 16, 17, 18, 19, 97, 100]
    for value in test_values:
        print(f"{value}: {is_prime(value)}")