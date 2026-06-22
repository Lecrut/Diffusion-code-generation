def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, 10, 13, 15, 17, 18, 19, 20, 97, 100, 0, 1, -5]
    results = {val: is_prime(val) for val in test_values}
    for val in test_values:
        print(is_prime(val))