import random

def get_random_element(lst):
    if not lst:
        raise IndexError("Cannot select from an empty list")
    index = random.randrange(len(lst))
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_random_element(sample_list)
    print(result)