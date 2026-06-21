def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def group_numbers(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if not is_prime(num) and num >= 2]
    return {'primes': primes, 'composites': composites}

if __name__ == '__main__':
    sample_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = group_numbers(sample_numbers)
    print(result)