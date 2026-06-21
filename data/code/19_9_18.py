import random
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def get_random_element(frozen_structure):
    index = random.randint(0, len(frozen_structure) - 1)
    return frozen_structure[index]

if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    p3 = Point(50, 60)
    structure = (p1, p2, p3)
    result = get_random_element(structure)
    print(result)