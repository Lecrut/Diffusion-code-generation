def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n ** 0.5) + 1
    step = 2
    factor = 5
    while factor <= limit:
        if n % factor == 0:
            return False
        factor += step
        step = 6 - step
    return True

if __name__ == '__main__':
    test_cases = [2, 3, 4, 5, 10, 11, 12, 13, 100, 101, 541, 542, 1009, 1010]
    results = []
    for num in test_cases:
        results.append((num, is_prime(num)))
    for num, result in results:
        print(f"{num}: {result}")