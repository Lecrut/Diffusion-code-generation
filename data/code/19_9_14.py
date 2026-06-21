import random
from collections import namedtuple

def random_element_from_namedtuple(nt_instance):
    return random.choice(nt_instance)

if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    result = random_element_from_namedtuple(p)
    print(result)