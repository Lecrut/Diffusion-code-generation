import random

def get_random_element(lst):
    if not lst:
        return None
    return lst[random.randint(0, len(lst) - 1)]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_random_element(sample_list)
    print(result)