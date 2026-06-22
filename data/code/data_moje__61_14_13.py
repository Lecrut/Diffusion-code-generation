def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, 16, 17, 19, 20, 23, 24, 29, 30, 37, 49, 97, 100]
    results = {value: is_prime(value) for value in test_values}
    for value, prime_status in results.items():
        print(f"{value}: {prime_status}")