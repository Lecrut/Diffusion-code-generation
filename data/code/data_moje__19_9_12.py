import random
import sys
from collections import namedtuple

def random_element_from_frozen(frozen_data):
    indices = [i for i in range(len(frozen_data))]
    idx = random.choice(indices)
    return frozen_data[idx]

Point = namedtuple('Point', ['x', 'y'])

def main():
    p = Point(10, 20)
    val = random_element_from_frozen(p)
    print(val)

if __name__ == '__main__':
    main()