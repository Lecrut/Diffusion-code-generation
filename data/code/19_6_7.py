import random

def get_random_element_from_set(s):
    lst = list(s)
    return random.choice(lst)

if __name__ == '__main__':
    sample_set = {10, 20, 30, 40, 50}
    result = get_random_element_from_set(sample_set)
    print(result)