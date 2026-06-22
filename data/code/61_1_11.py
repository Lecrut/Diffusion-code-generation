def is_prime(n):
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

def get_primes_less_than_sqrt(n):
    if n <= 2:
        return []
    limit = int(n ** 0.5)
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def check_primality_by_primes(n):
    if n <= 1:
        return False
    primes = get_primes_less_than_sqrt(n)
    for p in primes:
        if n % p == 0:
            if n != p:
                return False
    return True

if __name__ == '__main__':
    test_numbers = [1, 2, 3, 4, 17, 18, 97, 100, 7919]
    for num in test_numbers:
        result = check_primality_by_primes(num)
        print(f"{num}: {result}")
    
    smaller_tests = [2, 3, 5, 10, 25, 49, 121]
    for num in smaller_tests:
        result = is_prime(num)
        print(f"Direct {num}: {result}")