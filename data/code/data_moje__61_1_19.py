def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    primes = [2]
    candidate = 3
    while candidate * candidate <= n:
        is_candidate_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_candidate_prime = False
                break
        if is_candidate_prime:
            primes.append(candidate)
        if candidate % p == 0:
            return False
        candidate += 2
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, 10, 17, 20, 23, 97, 100]
    for val in test_values:
        print(is_prime(val))