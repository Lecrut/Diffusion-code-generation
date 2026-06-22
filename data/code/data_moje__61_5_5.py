def is_prime(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    if n <= 3:
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
    print(is_prime(29))
    print(is_prime(10))
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(97))