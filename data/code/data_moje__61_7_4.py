import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes(numbers):
    results = {}
    for num in numbers:
        results[num] = is_prime(num)
    return results

if __name__ == '__main__':
    sample_values = [2, 3, 4, 17, 18, 19, 97, 100, 101, 1009]
    results = check_primes(sample_values)
    print(results)