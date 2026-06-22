import random

def find_min_value(numbers):
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [random.randint(1, 100) for _ in range(10)]
    print(find_min_value(sample_numbers))