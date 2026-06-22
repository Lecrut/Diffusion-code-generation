import random

def generate_random_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    sample_count = 10
    random_numbers = generate_random_numbers(sample_count)
    print("Original list:", random_numbers)
    reverse_list(random_numbers)
    print("Reversed list:", random_numbers)