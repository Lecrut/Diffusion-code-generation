from collections import namedtuple
from random import choice

Point = namedtuple('Point', ['x', 'y'])

def get_random_field_value(frozen_obj):
    field_names = frozen_obj._fields
    selected_field = choice(field_names)
    return getattr(frozen_obj, selected_field)

if __name__ == '__main__':
    p = Point(10, 20)
    result = get_random_field_value(p)
    print(result)