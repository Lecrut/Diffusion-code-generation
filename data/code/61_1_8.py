def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    primes = [2]
    candidate = 3
    while candidate * candidate <= n:
        if candidate * candidate <= n:
            limit = int(candidate ** 0.5) + 1
            is_prime_candidate = True
            for p in primes:
                if p > limit:
                    break
                if candidate % p == 0:
                    is_prime_candidate = False
                    break
            if is_prime_candidate:
                primes.append(candidate)
        candidate += 2
    
    limit = int(n ** 0.5)
    for p in primes:
        if p > limit:
            break
        if n % p == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 17, 20, 23, 97, 100, 101]
    for val in test_values:
        print(val, is_prime(val))