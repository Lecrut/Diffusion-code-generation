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

    def __contains__(self, name):
        return any((item.name == name for item in self._mapping))

    def __iter__(self):
        return (item.name for item in self._mapping)

    def __len__(self):
        return len(self._mapping)
if __name__ == '__main__':
    fm = FrozenMapping(('a', 1), ('b', 2))
    print(fm['a'])
    print('c' in fm)
    for key in fm:
        print(key, fm[key])
    print(len(fm))