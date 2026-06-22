import random

def get_random_element(lst):
    if not lst:
        raise IndexError("Cannot select from an empty list")
    return lst[random.randrange(len(lst))]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(get_random_element(sample_list))