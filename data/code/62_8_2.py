def find_divisors(n):
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
        i += 1
    return sorted(divs)

if __name__ == '__main__':
    target = 999999
    result = find_divisors(target)
    print(result)