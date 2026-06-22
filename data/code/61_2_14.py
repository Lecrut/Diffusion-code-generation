def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 9, 11, 15, 17, 97, 100]
    for val in test_values:
        print(is_prime(val))