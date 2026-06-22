import math

def find_divisors(n):
    divisors = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    result = find_divisors(1024)
    print(result)