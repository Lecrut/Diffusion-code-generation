def get_factors(n):
    small_factors = (i for i in range(1, int(n**0.5) + 1) if n % i == 0)
    large_factors = (n // i for i in range(1, int(n**0.5) + 1) if n % i == 0)
    all_factors = set()
    for f in small_factors:
        all_factors.add(f)
    for f in large_factors:
        all_factors.add(f)
    return sorted(all_factors)

if __name__ == '__main__':
    print(get_factors(120))