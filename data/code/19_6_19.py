import random

def get_random_element(input_set):
    if not input_set:
        return None
    element_list = list(input_set)
    return element_list[random.randint(0, len(element_list) - 1)]

if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5}
    result = get_random_element(sample_set)
    print(result)