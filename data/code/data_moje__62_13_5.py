def get_divisors(n):
    if n == 0:
        return []
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

if __name__ == '__main__':
    number = 100
    result = get_divisors(number)
    print(result)