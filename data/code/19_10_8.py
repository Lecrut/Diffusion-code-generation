import random

def get_random_element(input_list):
    lookup_map = {index: value for index, value in enumerate(input_list)}
    selected_index = random.randint(0, len(lookup_map) - 1)
    return lookup_map[selected_index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    result = get_random_element(sample_list)
    print(result)