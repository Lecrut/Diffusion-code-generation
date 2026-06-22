def is_prime(n):
    if n < 2:
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
    sample_values = [0, 1, 2, 3, 4, 10, 17, 19, 20, 25, 29, 97, 99, 100, 101, 179, 180, 181]
    results = [is_prime(n) for n in sample_values]
    print(results)