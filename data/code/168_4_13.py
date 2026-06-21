def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def group_numbers(numbers):
    categories = {'primes': [], 'composites': []}
    for num in numbers:
        category = 'primes' if is_prime(num) else 'composites'
        categories[category].append(num)
    return categories

if __name__ == '__main__':
    sample_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(group_numbers(sample_numbers))