def _has_odd_factor(n):
    limit = int(n**0.5)
    candidate = 3
    while candidate <= limit:
        if n % candidate == 0:
            return True
        candidate += 2
    return False

def is_prime(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return not _has_odd_factor(n)

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 17, 18, 19, 20, 97, 100]
    for value in test_values:
        print(is_prime(value))