def classify_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime = []
    composite = []

    for number in numbers:
        if is_prime(number):
            prime.append(number)
        else:
            composite.append(number)

    return {'prime': prime, 'composite': composite}

if __name__ == '__main__':
    sample_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = classify_numbers(sample_numbers)
    print(result)