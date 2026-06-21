import random

def get_random_element(lst):
    if not lst:
        raise IndexError("Cannot select from an empty list")
    return lst[random.randrange(len(lst))]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_random_element(sample_list)
    print(result)