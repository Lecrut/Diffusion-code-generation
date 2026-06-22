def get_divisors(n):
    if n == 0:
        return []
    if n < 0:
        n = -n
    divs = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
        i += 1
    return sorted(divs)

if __name__ == '__main__':
    result = get_divisors(36)
    print(result)