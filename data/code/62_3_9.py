def get_divisors(n):
    if n == 1:
        return [1]
    divs = [d for d in range(1, n + 1) if n % d == 0]
    return divs

if __name__ == '__main__':
    print(get_divisors(1))