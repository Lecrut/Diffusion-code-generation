import random

def generate_random_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def reverse_list(lst):
    length = len(lst)
    for i in range(length // 2):
        lst[i], lst[length - i - 1] = lst[length - i - 1], lst[i]

if __name__ == '__main__':
    sample_count = 10
    random_numbers = generate_random_numbers(sample_count)
    print("Original list:", random_numbers)
    reverse_list(random_numbers)
    print("Reversed list:", random_numbers)