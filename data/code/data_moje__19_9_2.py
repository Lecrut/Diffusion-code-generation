import random
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])

def random_access_namedtuple(named_tuple):
    random_index = random.randrange(0, len(named_tuple))
    return named_tuple[random_index]

if __name__ == '__main__':
    sample_point = Point(1, 2, 3)
    result = random_access_namedtuple(sample_point)
    print(result)