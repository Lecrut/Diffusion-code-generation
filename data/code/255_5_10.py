import random

def find_max_value(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_numbers = [random.randint(1, 100) for _ in range(10)]
    print("Original List:", sample_numbers)
    print("Maximum Value:", find_max_value(sample_numbers))