def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def group_numbers(numbers):
    primes = []
    composites = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        else:
            composites.append(num)
    return {'primes': primes, 'composites': composites}

if __name__ == '__main__':
    sample_numbers = [2, 3, 5, 7, 10, 12, 14, 16, 18]
    result = group_numbers(sample_numbers)
    print(result)