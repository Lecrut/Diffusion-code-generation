def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

if __name__ == '__main__':
    print(is_prime(7))
    print(is_prime(4))
    print(is_prime(1))
    print(is_prime(2))