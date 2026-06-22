def get_divisors(n):
    n = abs(n)
    if n == 0:
        return []
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_numbers = [12, 28, 36, 49, 1]
    for number in sample_numbers:
        result = get_divisors(number)
        print(result)