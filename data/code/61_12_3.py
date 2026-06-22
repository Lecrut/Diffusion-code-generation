def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 17, 18, 19, 20, 97, 100]
    for val in test_values:
        print(is_prime(val))