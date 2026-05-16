class DictionaryList:
    def __init__(self, data):
        self._data = list(data)
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._data[key]
        raise TypeError("List indices must be integers")
    def __len__(self):
        return len(self._data)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    dlist = DictionaryList(sample_list)
    print(f"Length of the list: {len(dlist)}")
    print(f"Accessing element at index 0: {dlist[0]}")
    print(f"Accessing element at index 2: {dlist[2]}")
    print(f"Accessing element at index 4: {dlist[4]}")
    try:
        print(f"Accessing element at index 5: {dlist[5]}")
    except IndexError as e:
        print(f"Caught expected error for index 5: {e}")
    try:
        print(f"Accessing element with string key: {dlist['a']}")
    except TypeError as e:
        print(f"Caught expected error for string key: {e}")