def find_factors(n):
    small_factors = (i for i in range(1, int(n**0.5) + 1) if n % i == 0)
    large_factors = (n // i for i in reversed(list(small_factors)) if i * (n // i) == n)
    seen = set()
    result = []
    for factor in chain(small_factors, large_factors):
        if factor not in seen:
            seen.add(factor)
            result.append(factor)
    return sorted(result)

from itertools import chain

if __name__ == '__main__':
    print(find_factors(120))