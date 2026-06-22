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
    samples = [1, 2, 3, 4, 17, 25, 29, 30, 97, 100]
    results = []
    for num in samples:
        results.append(is_prime(num))
    print(results)