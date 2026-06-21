def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    
    for number in range(2, int(limit ** 0.5) + 1):
        if is_prime[number]:
            for multiple in range(number*number, limit + 1, number):
                is_prime[multiple] = False
                
    return [num for num, prime in enumerate(is_prime) if prime]

if __name__ == '__main__':
    sample_limit = 30
    primes = sieve_of_eratosthenes(sample_limit)
    print(primes)