def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    primes = [2]
    i = 3
    while i * i <= n:
        is_prime_i = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                is_prime_i = False
                break
        if is_prime_i:
            primes.append(i)
        i += 2
    
    if primes[-1] * primes[-1] > n and primes[-1] > 1:
        primes = [p for p in primes if p * p <= n]
    
    if primes and primes[-1] * primes[-1] == n:
        return False
        
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    
    return True

if __name__ == '__main__':
    test_values = [2, 17, 18, 19, 97, 100, 101, 102, 997, 1000, 1009]
    results = []
    for val in test_values:
        result = is_prime(val)
        results.append((val, result))
    for val, res in results:
        print(f"{val}: {res}")