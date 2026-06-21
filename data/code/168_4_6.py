def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
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
    sample_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = group_numbers(sample_numbers)
    print(result)