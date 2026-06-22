def find_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

if __name__ == '__main__':
    number = 1024
    result = find_divisors(number)
    print(result)