def get_divisors(n):
    if n <= 0:
        return []
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return sorted(divs)

if __name__ == '__main__':
    result = get_divisors(100)
    print(result)