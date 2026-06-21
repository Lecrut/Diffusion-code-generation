from collections import namedtuple
NameValue = namedtuple('NameValue', ['name', 'value'])

class FrozenMapping:

    def __init__(self, pairs):
        self._mapping = tuple((NameValue(name, value) for name, value in pairs))

    def __getitem__(self, name):
        for pair in self._mapping:
            if pair.name == name:
                return pair.value
        raise KeyError(f"Key '{name}' not found")

    def __contains__(self, name):
        return any((pair.name == name for pair in self._mapping))

    def __iter__(self):
        return iter(((pair.name, pair.value) for pair in self._mapping))

    def __len__(self):
        return len(self._mapping)
if __name__ == '__main__':
    sample_pairs = [('a', 1), ('b', 2), ('c', 3)]
    fm = FrozenMapping(sample_pairs)
    print(fm['a'])
    print('b' in fm)
    for name, value in fm:
        print(f'{name}: {value}')