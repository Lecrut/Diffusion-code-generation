def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False
                
    return [num for num, prime in enumerate(is_prime) if prime]

if __name__ == '__main__':
    primes = sieve_of_eratosthenes(30)
    print(primes)