import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def find_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
if __name__ == '__main__':
    n = 10
    first_ten_primes = find_first_n_primes(n)
    total_sum = sum(first_ten_primes)
    print(total_sum)