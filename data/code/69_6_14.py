class ListDict:

    def __init__(self, initial_list=None):
        self._list = initial_list if initial_list is not None else []

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value

    def __len__(self):
        return len(self._list)
if __name__ == '__main__':
    ld = ListDict([10, 20, 30])
    print(ld[0])
    ld[1] = 25
    print(ld)
    print(len(ld))