def _is_perfect_square(n):
    if n < 0:
        return False
    root = int(n**0.5)
    if root * root == n:
        return True
    for r in (root - 1, root + 1):
        if r >= 0 and r * r == n:
            return True
    return False

def _handle_small_primes(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 25:
        return True
    if n < 121:
        return not (n % 5 == 0 or n % 7 == 0 or n % 11 == 0)
    if _is_perfect_square(n):
        return False
    return True

def _check_larger_primes(n):
    i = 11
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_prime(n):
    if not isinstance(n, int):
        return False
    if n < 0:
        return False
    if n < 121:
        return _handle_small_primes(n)
    return _check_larger_primes(n)

if __name__ == '__main__':
    test_cases = [10, 17, 29, 121, 127, 999999937]
    for val in test_cases:
        print(is_prime(val))