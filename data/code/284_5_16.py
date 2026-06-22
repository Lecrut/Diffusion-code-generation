import random

def generate_random_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def reverse_list(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

if __name__ == '__main__':
    sample_count = 10
    random_numbers = generate_random_numbers(sample_count)
    print("Original list:", random_numbers)
    reverse_list(random_numbers)
    print("Reversed list:", random_numbers)