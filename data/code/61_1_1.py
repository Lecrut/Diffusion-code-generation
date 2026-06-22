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
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_primes_up_to_sqrt(n):
    if n < 2:
        return []
    
    limit = int(n**0.5)
    if limit < 2:
        return []
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
        p += 1
    
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes

def check_primality_with_primes(n):
    if n < 2:
        return False
    
    primes = get_primes_up_to_sqrt(n)
    
    if n == 2:
        return True
        
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
            
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 10, 13, 29, 30, 97, 100, 101, 1000003, 1000033]
    
    for val in test_values:
        result = check_primality_with_primes(val)
        print(result)