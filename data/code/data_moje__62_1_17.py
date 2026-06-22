def compute_divisors(n: int) -> list:
    if n <= 0:
        return []
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return sorted(divisors)
if __name__ == '__main__':
    result = compute_divisors(100)
    print(result)