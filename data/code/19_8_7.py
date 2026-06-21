import random

def get_random_value_from_index(value_list):
    if not value_list:
        return None
    indices = range(len(value_list))
    random_index = random.choice(indices)
    return value_list[random_index]

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    result = get_random_value_from_index(numbers)
    print(result)