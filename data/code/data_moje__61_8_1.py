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
    test_values = [2, 3, 4, 17, 18, 19, 20, 23, 24, 29, 100, 101, 997, 999]
    for val in test_values:
        print(f"{val}: {is_prime(val)}")