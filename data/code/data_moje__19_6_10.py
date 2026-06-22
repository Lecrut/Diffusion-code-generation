import random

def get_random_element(input_set):
    element_list = list(input_set)
    if not element_list:
        return None
    return random.choice(element_list)

if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5}
    result = get_random_element(sample_set)
    print(result)