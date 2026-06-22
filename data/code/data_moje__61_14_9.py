def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
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
    test_values = [0, 1, 2, 3, 4, 5, 10, 11, 13, 15, 17, 20, 23, 29, 30, 97, 100, 7919, 8000]
    for val in test_values:
        print(f"is_prime({val}) = {is_prime(val)}")