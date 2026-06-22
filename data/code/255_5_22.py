import random

def find_max_value(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_list = [random.randint(1, 100) for _ in range(10)]
    print("Original List:", sample_list)
    max_val = find_max_value(sample_list)
    print("Maximum Value:", max_val)