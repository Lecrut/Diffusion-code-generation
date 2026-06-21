from collections import namedtuple
NameValue = namedtuple('NameValue', ['name', 'value'])

class FrozenMapping:

    def __init__(self, items):
        self._mapping = tuple((NameValue(name, value) for name, value in items))

    def __getitem__(self, key):
        for item in self._mapping:
            if item.name == key:
                return item.value
        raise KeyError(key)

    def __contains__(self, key):
        return any((item.name == key for item in self._mapping))

    def __iter__(self):
        return (item.name for item in self._mapping)

    def __len__(self):
        return len(self._mapping)
if __name__ == '__main__':
    sample_mapping = FrozenMapping([('a', 1), ('b', 2)])
    print(sample_mapping['a'])
    print('c' in sample_mapping)