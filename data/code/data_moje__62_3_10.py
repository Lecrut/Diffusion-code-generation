def get_divisors(n):
    if n == 1:
        return [1]
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    result = get_divisors(1)
    print(result)