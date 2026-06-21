import random

def get_random_element(s):
    lst = list(s)
    if not lst:
        raise ValueError("Cannot select from an empty set")
    return lst[random.randint(0, len(lst) - 1)]

if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5}
    print(get_random_element(sample_set))