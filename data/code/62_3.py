def get_divisors(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

if __name__ == '__main__':
    print(get_divisors(1))