import math

def find_factors(n):
    if n < 1:
        return []
    if n == 1:
        return [1]
    factors = []
    step = 1
    start = 2
    end = int(math.isqrt(n))
    for i in range(start, end + 1):
        if n % i == 0:
            factors.append(i)
            counterpart = n // i
            if counterpart != i:
                factors.append(counterpart)
    factors.append(1)
    if n != 1:
        factors.append(n)
    factors.sort()
    return factors

if __name__ == '__main__':
    number = 7919
    result = find_factors(number)
    print(result)