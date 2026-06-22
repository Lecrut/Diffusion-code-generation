import random
from collections import namedtuple

def random_access_namedtuple(data_tuple):
    if not data_tuple:
        raise ValueError("Cannot access element from empty tuple")
    index = random.randint(0, len(data_tuple) - 1)
    return data_tuple[index]

if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y', 'z'])
    sample_point = Point(10, 20, 30)
    result = random_access_namedtuple(sample_point)
    print(result)