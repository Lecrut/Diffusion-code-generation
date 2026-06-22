import random

MAX_LIST_SIZE = 100
MIN_VALUE = 1
MAX_VALUE = 1000

def generate_random_list(size):
    return [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(size)]

def find_maximum(lst):
    if not lst:
        raise ValueError("List is empty")
    max_value = lst[0]
    for value in lst[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    random_list = generate_random_list(MAX_LIST_SIZE)
    print("Random List:", random_list)
    max_value = find_maximum(random_list)
    print("Maximum Value:", max_value)