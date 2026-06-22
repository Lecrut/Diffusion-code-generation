def check_prime(n):
    if not isinstance(n, int):
        return False
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
    print(check_prime(29))
    print(check_prime(10))
    print(check_prime(1))
    print(check_prime(0))
    print(check_prime(-5))