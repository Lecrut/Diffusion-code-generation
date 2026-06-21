from collections import namedtuple
NameValue = namedtuple('NameValue', ['name', 'value'])

class FrozenMapping:

    def __init__(self, items):
        self._items = tuple((NameValue(name, value) for name, value in items))

    def __getitem__(self, name):
        for item in self._items:
            if item.name == name:
                return item.value
        raise KeyError(name)

    def __contains__(self, name):
        return any((item.name == name for item in self._items))

    def __iter__(self):
        return (item.name for item in self._items)

    def __len__(self):
        return len(self._items)
if __name__ == '__main__':
    sample_mapping = FrozenMapping([('a', 1), ('b', 2)])
    print(sample_mapping['a'])
    print('c' in sample_mapping)