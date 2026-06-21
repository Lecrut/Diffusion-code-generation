MAX_NUMBER = 100

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number*number, limit + 1, number):
                is_prime[multiple] = False
                
    return [num for num, prime in enumerate(is_prime) if prime]

if __name__ == '__main__':
    primes = sieve_of_eratosthenes(MAX_NUMBER)
    print(primes)