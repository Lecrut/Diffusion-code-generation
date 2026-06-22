def find_divisors(n):
    divisors = []
    step = 1 if n % 2 != 0 else 1
    limit = int(n**0.5)
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    number = 999999
    result = find_divisors(number)
    print(result)