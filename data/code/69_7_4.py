class DictionaryList:
    def __init__(self, data):
        self._data = list(data)
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._data[key]
        raise TypeError("Index must be an integer")
    def __len__(self):
        return len(self._data)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    dlist = DictionaryList(sample_list)
    print(f"Length of the list: {len(dlist)}")
    print(f"Element at index 0: {dlist[0]}")
    print(f"Element at index 2: {dlist[2]}")
    print(f"Element at index 4: {dlist[4]}")
    try:
        print(f"Element at index 10: {dlist[10]}")
    except IndexError as e:
        print(f"Caught expected error: {e}")
    try:
        print(f"Element with non-integer key 'a': {dlist['a']}")
    except TypeError as e:
        print(f"Caught expected error: {e}")