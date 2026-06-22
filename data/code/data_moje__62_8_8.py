def find_divisors(n):
    if n < 1:
        return []
    divs = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
        i += 1
    return sorted(divs)

if __name__ == '__main__':
    result = find_divisors(999999)
    print(result)