import random
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])

def get_random_field(obj):
    fields = obj._fields
    if not fields:
        raise ValueError("The named tuple has no fields")
    random_index = random.randint(0, len(fields) - 1)
    return obj[random_index]

if __name__ == '__main__':
    sample_point = Point(10, 20, 30)
    result = get_random_field(sample_point)
    print(result)