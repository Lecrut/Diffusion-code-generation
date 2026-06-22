def get_divisors(n):
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
    sample_values = [12, 28, 100, 1, 97]
    for val in sample_values:
        print(get_divisors(val))