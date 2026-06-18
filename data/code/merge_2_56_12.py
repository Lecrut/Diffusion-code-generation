import math
def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0: return False
    return True
def prime_factors(num):
    factors = {}
    d = 2
    temp = num
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1 if d == 2 else 2
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors
def get_prime_index(num):
    sorted_factors = sorted(factors.items())
if __name__ == '__main__':
    target_num = 756
    f = prime_factors(target_num)
    sorted_items = sorted(f.items(), reverse=True)
    target_prime_base, _ = sorted_items[0]
    print(target_num)