def get_factors(n):
    small = (i for i in range(1, int(n**0.5) + 1) if n % i == 0)
    for i in small:
        yield i
    large = (n // i for i in small if i != n // i)
    for i in reversed(list(large)):
        yield i

if __name__ == '__main__':
    print(list(get_factors(120)))