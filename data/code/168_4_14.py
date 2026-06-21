def group_numbers(numbers):
    primes = []
    composites = []
    for num in numbers:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        (primes if is_prime else composites).append(num)
    return {'primes': primes, 'composites': composites}

if __name__ == '__main__':
    sample_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(group_numbers(sample_numbers))