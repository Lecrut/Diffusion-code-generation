def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    primes = [2, 3]
    candidate = 5
    while candidate * candidate <= n:
        is_candidate_prime = True
        for p in primes:
            if candidate % p == 0:
                is_candidate_prime = False
                break
        if is_candidate_prime:
            primes.append(candidate)
            if candidate * candidate > n:
                break
        candidate += 2
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, 17, 18, 19, 97, 100, 101]
    for value in test_values:
        result = is_prime(value)
        print(f"{value}: {result}")