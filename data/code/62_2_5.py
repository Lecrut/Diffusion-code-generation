def find_factors(number):
    if number <= 0:
        return []
    factors = []
    limit = int(number ** 0.5)
    for i in range(1, limit + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    factors.sort()
    return factors

if __name__ == '__main__':
    target_prime = 7919
    result = find_factors(target_prime)
    print(result)