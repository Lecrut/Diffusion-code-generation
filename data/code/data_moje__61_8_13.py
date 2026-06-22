def is_prime(n: int) -> bool:
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
    test_values = [2, 3, 4, 17, 18, 19, 20, 97, 100]
    results = [is_prime(x) for x in test_values]
    for val, res in zip(test_values, results):
        print(f"{val}: {res}")