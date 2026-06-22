import random

ZERO_LENGTH_THRESHOLD = 0

def get_random_element_from_set(input_set):
    if len(input_set) <= ZERO_LENGTH_THRESHOLD:
        return None
    list_version = list(input_set)
    list_size = len(list_version)
    random_position = random.randint(0, list_size - 1)
    return list_version[random_position]

if __name__ == '__main__':
    demo_data = {"red", "green", "blue", "yellow", "purple"}
    selected_item = get_random_element_from_set(demo_data)
    print(selected_item)
    empty_data = set()
    empty_result = get_random_element_from_set(empty_data)
    print(empty_result)