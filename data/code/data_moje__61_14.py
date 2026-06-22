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
    test_numbers = [1, 2, 3, 4, 5, 16, 17, 19, 20, 23, 24, 25, 29, 30, 97, 100]
    results = []
    for number in test_numbers:
        results.append((number, is_prime(number)))
    for number, prime_status in results:
        print(f"{number}: {prime_status}")