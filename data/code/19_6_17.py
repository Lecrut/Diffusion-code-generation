import random

def get_random_element_from_set(data_set: set):
    return random.choice(list(data_set))

if __name__ == '__main__':
    sample_set = {10, 20, 30, 40, 50}
    result = get_random_element_from_set(sample_set)
    print(result)