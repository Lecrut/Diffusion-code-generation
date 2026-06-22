def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
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
    print(is_prime(2))
    print(is_prime(17))
    print(is_prime(18))
    print(is_prime(-5))
    print(is_prime(0))
    print(is_prime(1))