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

def find_primes_up_to(n):
    if n < 2:
        return []
    primes = [2]
    for i in range(3, n + 1, 2):
        if is_prime(i):
            primes.append(i)
    return primes

def check_primality_with_primes(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    import math
    limit = int(math.sqrt(n)) + 1
    primes = find_primes_up_to(limit)
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, 10, 17, 18, 19, 20, 97, 100, 101, 103, 104]
    for val in test_values:
        result = check_primality_with_primes(val)
        print(f"{val}:{result}")