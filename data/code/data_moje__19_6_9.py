import random

def get_random_element(input_set):
    if not input_set:
        return None
    lst = list(input_set)
    idx = random.randint(0, len(lst) - 1)
    return lst[idx]

if __name__ == '__main__':
    sample_data = {10, 20, 30, 40, 50}
    print(get_random_element(sample_data))