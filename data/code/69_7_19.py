class CustomList:

    def __init__(self, data):
        self._data = list(data)

    def get_sublist(self, start_index, end_index):
        if not (isinstance(start_index, int) and isinstance(end_index, int)):
            raise TypeError('Start and end indices must be integers')
        if start_index < 0 or end_index >= len(self._data) or start_index > end_index:
            return []
        return self._data[start_index:end_index + 1]
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    clist = CustomList(sample_list)
    print(clist.get_sublist(1, 3))
    print(clist.get_sublist(0, 4))
    print(clist.get_sublist(2, 2))
    print(clist.get_sublist(5, 10))
    print(clist.get_sublist(-1, 2))