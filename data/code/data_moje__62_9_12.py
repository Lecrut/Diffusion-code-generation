def get_divisors(n):
    if n <= 0:
        return []
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
    sample_numbers = [12, 28, 100, 13, 1]
    for num in sample_numbers:
        print(get_divisors(num))