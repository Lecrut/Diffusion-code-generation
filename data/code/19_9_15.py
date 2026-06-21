import random
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])

def random_element_from_namedtuple(data):
    if not data:
        return None
    index = random.randint(0, len(data) - 1)
    return data[index]

if __name__ == '__main__':
    sample_point = Point(10, 20, 30)
    result = random_element_from_namedtuple(sample_point)
    print(result)