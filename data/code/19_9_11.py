import random
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])

def get_random_element(data):
    index = random.randint(0, len(data) - 1)
    return data[index]

if __name__ == '__main__':
    sample_point = Point(10, 20, 30)
    result = get_random_element(sample_point)
    print(result)