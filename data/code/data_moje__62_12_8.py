def get_divisors(n):
    divisors = []
    if n == 0:
        return divisors
    abs_n = abs(n)
    for i in range(1, int(abs_n ** 0.5) + 1):
        if abs_n % i == 0:
            divisors.append(i)
            if i != abs_n // i:
                divisors.append(abs_n // i)
    if n < 0:
        divisors.extend([-d for d in divisors])
    divisors.sort()
    return divisors

if __name__ == '__main__':
    sample_number = 28
    result = get_divisors(sample_number)
    print(result)