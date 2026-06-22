def get_divisors(n):
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
        i += 1
    divs.sort()
    return divs

if __name__ == '__main__':
    print(get_divisors(28))
    print(get_divisors(100))