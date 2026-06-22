def get_divisors_of_60():
    n = 60
    if n <= 0:
        raise ValueError("Number must be positive")
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
    print(get_divisors_of_60())