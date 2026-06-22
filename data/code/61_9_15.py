def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5) + 1
    i = 3
    while i < limit:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, 17, 18, 19, 97, 100, 101, 1000]
    results = [is_prime(val) for val in test_values]
    print(results)