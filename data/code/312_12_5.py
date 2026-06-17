class MaxList:
    def __init__(self, data):
        self._data = list(data)
        self._max_element = None
    def set_list(self, new_data):
        self._data = list(new_data)
        if not self._data:
            self._max_element = None
        else:
            self._max_element = max(self._data)
    def get_max(self):
        return self._max_element
if __name__ == '__main__':
    sample1 = [10, 5, 20, 8]
    ml1 = MaxList(sample1)
    print(f"Max for {sample1}: {ml1.get_max()}")
    sample2 = [3, 1, 4, 1, 5, 9, 2, 6]
    ml2 = MaxList(sample2)
    print(f"Max for {sample2}: {ml2.get_max()}")
    new_sample1 = [1, 100, 50]
    ml1.set_list(new_sample1)
    print(f"Max for {new_sample1}: {ml1.get_max()}")
    new_sample2 = []
    ml2.set_list(new_sample2)
    print(f"Max for {new_sample2}: {ml2.get_max()}")