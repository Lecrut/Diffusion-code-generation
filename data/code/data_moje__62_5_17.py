def find_factors(n):
    small_factors = []
    large_factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            small_factors.append(i)
            if i != n // i:
                large_factors.append(n // i)
    large_factors.reverse()
    return small_factors + large_factors

if __name__ == '__main__':
    print(find_factors(120))