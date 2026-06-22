def get_divisors(n):
    return [i for i in range(1, int(n**0.5) + 1) if n % i == 0]

def get_all_divisors(n):
    divs = []
    small_divs = get_divisors(n)
    large_divs = []
    for d in small_divs:
        divs.append(d)
        if d * d != n:
            large_divs.append(n // d)
    large_divs.reverse()
    return divs + large_divs

if __name__ == '__main__':
    print(get_all_divisors(60))