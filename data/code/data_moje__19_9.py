import random
from collections import namedtuple

def random_access_namedtuple(record):
    index = random.randint(0, len(record) - 1)
    return record[index]

if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y', 'z'])
    sample_point = Point(10, 20, 30)
    result = random_access_namedtuple(sample_point)
    print(result)