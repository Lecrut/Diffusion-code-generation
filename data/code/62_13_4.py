from math import isqrt

def get_divisors(n):
    if n <= 0:
        return []
    divs = []
    limit = isqrt(n)
    for i in range(1, limit + 1):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    divs.sort()
    return divs

if __name__ == '__main__':
    value = 360
    result = get_divisors(value)
    print(result)