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
    test_values = [2, 3, 4, 5, 16, 17, 18, 19, 20, 23, 25, 29, 97, 100, 101, 541, 542]
    results = []
    for num in test_values:
        results.append((num, is_prime(num)))
    for num, prime in results:
        print(f"{num}: {prime}")