def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))

if __name__ == '__main__':
    print(is_prime(17))
    print(is_prime(18))
    print(is_prime(2))
    print(is_prime(1))
    print(is_prime(97))