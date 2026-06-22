from math import sqrt

def get_divisors(n):
    if n <= 0:
        return []
    divisors = set()
    limit = int(sqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors))

if __name__ == '__main__':
    number = 28
    divisors = get_divisors(number)
    print(divisors)