import random

def random_element_from_set(input_set):
    if not input_set:
        return None
    element_list = list(input_set)
    return random.choice(element_list)

if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5}
    result = random_element_from_set(sample_set)
    print(result)