import random
from collections import namedtuple

def get_random_element_from_namedtuple(data_tuple):
    if len(data_tuple) == 0:
        raise IndexError("Cannot access element from an empty tuple")
    random_index = random.randint(0, len(data_tuple) - 1)
    return data_tuple[random_index]

if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y', 'z'])
    sample_point = Point(10, 20, 30)
    result = get_random_element_from_namedtuple(sample_point)
    print(result)