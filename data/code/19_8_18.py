import random

def get_random_value(numbers):
    indices = range(len(numbers))
    random_index = random.choice(indices)
    return numbers[random_index]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = get_random_value(sample_numbers)
    print(result)