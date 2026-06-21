from collections import namedtuple
NameValue = namedtuple('NameValue', ['name', 'value'])

class FrozenMapping:

    def __init__(self, *items):
        self._mapping = tuple((NameValue(name, value) for name, value in items))

    def __getitem__(self, name):
        for item in self._mapping:
            if item.name == name:
                return item.value
        raise KeyError(name)

    def __hash__(self):
        return hash(self._mapping)

    def __eq__(self, other):
        if isinstance(other, FrozenMapping):
            return self._mapping == other._mapping
        return False
if __name__ == '__main__':
    fm = FrozenMapping(('a', 1), ('b', 2))
    print(fm['a'])
    print(fm['b'])