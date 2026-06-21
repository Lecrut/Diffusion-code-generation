import collections
import random

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

def get_random_element(coord):
    idx = random.randrange(len(coord))
    return coord[idx]

if __name__ == '__main__':
    point = Coordinate(10, 20)
    result = get_random_element(point)
    print(result)