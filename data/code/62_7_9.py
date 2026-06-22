def get_divisors(n):
    if n == 0:
        return []
    divisors = []
    limit = int(abs(n) ** 0.5)
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    result = get_divisors(0)
    print(result)
    result = get_divisors(10)
    print(result)