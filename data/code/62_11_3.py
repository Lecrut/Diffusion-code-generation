import math

def find_divisors(n):
    if n <= 0:
        return []
    divisors = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_values = [28, 1, 100, 0, -5]
    for n in sample_values:
        result = find_divisors(n)
        print(result)