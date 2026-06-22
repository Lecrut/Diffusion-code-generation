import random

def generate_random_integers(count):
    return [random.randint(1, 100) for _ in range(count)]

def find_maximum_value(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample_count = 10
    random_numbers = generate_random_integers(sample_count)
    max_value = find_maximum_value(random_numbers)
    print("Random Numbers:", random_numbers)
    print("Maximum Value:", max_value)