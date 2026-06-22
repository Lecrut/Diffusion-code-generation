import math

def get_divisors(n):
    if n <= 0:
        return []
    divisors = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    sample_number = 100
    result = get_divisors(sample_number)
    print(result)