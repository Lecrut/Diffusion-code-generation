def is_prime(n):
    if n <= 1:
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
    test_values = [1, 2, 3, 4, 17, 18, 19, 20, 97, 100]
    for val in test_values:
        result = is_prime(val)
        print(result)