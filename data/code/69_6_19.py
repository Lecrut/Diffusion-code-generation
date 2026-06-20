class ListDict:

    def __init__(self, initial_list=None):
        self._list = initial_list if initial_list is not None else []

    def __getitem__(self, key):
        return self._list[key]

    def __setitem__(self, key, value):
        self._list[key] = value

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        return iter(self._list)
if __name__ == '__main__':
    ld = ListDict([10, 20, 30])
    print(ld[0])
    ld[1] = 25
    print(ld)
    print(len(ld))