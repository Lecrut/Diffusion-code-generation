def divisors(n):
    if n == 0:
        return []
    if n < 0:
        n = -n
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)

if __name__ == '__main__':
    print(divisors(0))
    print(divisors(12))
    print(divisors(7))
    print(divisors(-15))