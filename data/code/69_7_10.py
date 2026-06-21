class DictionaryList:
    def __init__(self, data):
        self._data = list(data)

    def get_sublist(self, start_index, end_index):
        if not (isinstance(start_index, int) and isinstance(end_index, int)):
            raise TypeError("Start and end indices must be integers")
        if start_index < 0 or end_index >= len(self._data) or start_index > end_index:
            raise IndexError("Invalid start or end index")
        return self._data[start_index:end_index + 1]

    def __len__(self):
        return len(self._data)

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    dlist = DictionaryList(sample_list)
    print(f"Length of the list: {len(dlist)}")
    sublist = dlist.get_sublist(1, 3)
    print(f"Sublist from index 1 to 3: {sublist}")
    try:
        invalid_sublist = dlist.get_sublist(5, 7)
        print(f"Invalid sublist: {invalid_sublist}")
    except IndexError as e:
        print(e)
    try:
        type_error_sublist = dlist.get_sublist('a', 'b')
        print(f"Type error sublist: {type_error_sublist}")
    except TypeError as e:
        print(e)