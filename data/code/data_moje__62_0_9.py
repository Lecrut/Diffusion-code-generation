import math

def get_divisors(n):
    divisors = []
    i = 1
    while i <= math.isqrt(n):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

if __name__ == '__main__':
    number = 36
    result = get_divisors(number)
    print(result)