import math

def get_divisors(n):
    if n <= 0:
        return []
    divisors = []
    sqrt_n = int(math.isqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    target_number = 999999
    result = get_divisors(target_number)
    print(result)