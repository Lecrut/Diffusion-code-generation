def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def get_primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 15, 17, 25, 29, 97, 100]
    for val in sample_values:
        print(f"is_prime({val}) = {is_prime(val)}")
    primes_under_50 = get_primes_up_to(50)
    print(f"Primes under 50: {primes_under_50}")