def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
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
    samples = [1, 2, 3, 4, 17, 18, 97, 100]
    results = [is_prime(n) for n in samples]
    print(results)