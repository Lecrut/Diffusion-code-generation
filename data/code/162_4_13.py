from collections import namedtuple
Fruit = namedtuple('Fruit', ['name', 'type'])
Vegetable = namedtuple('Vegetable', ['name', 'color'])
FrozenMapping = {'apple': Fruit('apple', 'fruit'), 'banana': Fruit('banana', 'fruit'), 'carrot': Vegetable('carrot', 'orange')}
if __name__ == '__main__':
    print(FrozenMapping['apple'])
    print(FrozenMapping['carrot'])