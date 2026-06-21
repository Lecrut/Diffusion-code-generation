import random

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers = [random.randint(1, 100) for _ in range(50)]
    print(find_largest(sample_numbers))