def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
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
    test_values = [2, 3, 4, 17, 18, 19, 1, 0, -5, 97]
    for val in test_values:
        result = is_prime(val)
        print(f"{val}: {result}")