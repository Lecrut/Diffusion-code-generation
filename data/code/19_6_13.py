import random

def get_random_element_from_set(input_set):
    if not input_set:
        return None
    elements_list = list(input_set)
    random_index = random.randint(0, len(elements_list) - 1)
    return elements_list[random_index]

if __name__ == '__main__':
    sample_set = {10, 20, 30, 40, 50}
    result = get_random_element_from_set(sample_set)
    print(result)