import random
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

def random_access(element):
    length = len(element)
    index = random.randint(0, length - 1)
    return element[index]

if __name__ == '__main__':
    p = Point(10, 20)
    print(random_access(p))