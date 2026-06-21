import random
from collections import namedtuple

def random_access_namedtuple(namedtuple_instance):
    index = random.randint(0, len(namedtuple_instance) - 1)
    return namedtuple_instance[index]

if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y', 'z'])
    p = Point(1, 2, 3)
    result = random_access_namedtuple(p)
    print(result)