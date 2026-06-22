import random
from collections import namedtuple

def random_access_namedtuple(data, index=None):
    if index is None:
        index = random.randint(0, len(data) - 1)
    return data[index]

if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y', 'z'])
    sample_point = Point(10, 20, 30)
    result = random_access_namedtuple(sample_point)
    print(result)
    random_index = random.randint(0, 2)
    explicit_result = random_access_namedtuple(sample_point, random_index)
    print(explicit_result)