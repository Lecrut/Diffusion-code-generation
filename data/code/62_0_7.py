VALIDATION_CONSTANTS = {'min_val': 1}

def find_divisors(n):
    if not isinstance(n, int) or n < VALIDATION_CONSTANTS['min_val']:
        return []
    half_n = n // 2
    divisors = {1, n}
    limit = int(n ** 0.5)
    i = 2
    while i <= limit:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return sorted(divisors)

if __name__ == '__main__':
    target = 36
    output = find_divisors(target)
    print(output)