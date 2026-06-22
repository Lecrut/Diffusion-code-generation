def extract_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_number = 28
    result = extract_divisors(sample_number)
    print(result)