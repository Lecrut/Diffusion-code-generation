import random

def get_random_element(lst):
    if not lst:
        raise IndexError("Cannot select from empty list")
    idx = random.randint(0, len(lst) - 1)
    return lst[idx]

if __name__ == '__main__':
    data = [100, 200, 300, 400, 500]
    print(get_random_element(data))