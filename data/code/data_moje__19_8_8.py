import random

def get_random_value(int_list, range_obj):
    index = random.choice(list(range_obj))
    return int_list[index]

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    selection_range = range(10)
    result = get_random_value(numbers, selection_range)
    print(result)