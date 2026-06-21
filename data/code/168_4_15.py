def group_numbers(numbers):
    primes = []
    composites = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for number in numbers:
        if is_prime(number):
            primes.append(number)
        else:
            composites.append(number)

    return {'primes': primes, 'composites': composites}

if __name__ == '__main__':
    sample_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = group_numbers(sample_numbers)
    print(result)