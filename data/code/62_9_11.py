import math

def get_divisors(n):
    if n < 1:
        return []
    divisors = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_values = [1, 10, 28, 100, 17]
    for val in sample_values:
        print(get_divisors(val))