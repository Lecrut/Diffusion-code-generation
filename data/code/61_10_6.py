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
    test_values = [0, 1, 2, 3, 4, 5, 10, 13, 15, 17, 20, 23, 25, 29, 97, 100]
    for value in test_values:
        print(f"{value}: {is_prime(value)}")