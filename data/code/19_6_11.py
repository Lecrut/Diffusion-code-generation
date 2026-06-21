import random

def get_random_element_from_set(input_set):
    if not input_set:
        return None
    return random.choice(list(input_set))

if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5}
    result = get_random_element_from_set(sample_set)
    print(result)