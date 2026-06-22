def is_prime(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5) + 1
    divisor = 5
    while divisor <= limit:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

if __name__ == '__main__':
    print(is_prime(5431))
    print(is_prime(121))
    print(is_prime(2))
    print(is_prime(1))
    print(is_prime(0))