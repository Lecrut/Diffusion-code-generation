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
    test_numbers = [2, 3, 4, 17, 18, 29, 97, 100]
    results = {}
    for num in test_numbers:
        results[num] = is_prime(num)
    print(results)