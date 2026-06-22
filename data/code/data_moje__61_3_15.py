def _check_divisibility(n, limit, step):
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += step
    return True

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return _check_divisibility(n, n, 2)

if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(11))
    print(is_prime(15))
    print(is_prime(97))
    print(is_prime(100))
    print(is_prime(-7))