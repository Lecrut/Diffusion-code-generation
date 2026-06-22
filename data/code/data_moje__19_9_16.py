from collections import namedtuple
import random
import typing

Point = namedtuple('Point', ['x', 'y'])

def random_access_point(point: Point) -> typing.Any:
    index = random.randint(0, len(point) - 1)
    return point[index]

if __name__ == '__main__':
    p = Point(10, 20)
    result = random_access_point(p)
    print(result)