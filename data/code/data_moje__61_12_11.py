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
    test_values = [1, 2, 3, 4, 5, 17, 18, 19, 97, 99, 100, 101]
    for val in test_values:
        result = is_prime(val)
        print(result)