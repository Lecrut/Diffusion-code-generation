def generate_primes_up_to(limit):
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
    return primes

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    if n < 9:
        return True
    sqrt_n = int(n**0.5)
    primes = generate_primes_up_to(sqrt_n)
    for p in primes:
        if p <= sqrt_n:
            if n % p == 0:
                return False
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, 17, 18, 19, 20, 97, 100, 101, 1040, 1041, 1042]
    for val in test_values:
        result = is_prime(val)
        print(f"{val}: {result}")