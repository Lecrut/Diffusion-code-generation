def get_divisors(n: int) -> list[int]:
    if n == 1:
        return [1]
    divs: list[int] = [1, n]
    i = 2
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
        i += 1
    divs.sort()
    return divs

if __name__ == '__main__':
    print(get_divisors(1))