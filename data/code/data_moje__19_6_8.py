import random

def get_random_element(s):
    lst = list(s)
    if not lst:
        return None
    return random.choice(lst)

if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5}
    result = get_random_element(sample_set)
    print(result)