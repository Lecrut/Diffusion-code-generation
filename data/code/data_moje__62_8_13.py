import math

def find_divisors(n):
    if n <= 0:
        raise ValueError("Number must be positive")
    
    divisors = set()
    limit = int(math.isqrt(n))
    
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    
    return sorted(divisors)

if __name__ == '__main__':
    result = find_divisors(999999)
    print(result)