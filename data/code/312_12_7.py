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
    initial_list = [10, 5, 20, 8, 15]
    ml = MaxList(initial_list)
    print(f"Initial max: {ml.get_max()}")
    updated_list_1 = [30, 1, 15, 50, 2]
    ml.set_list(updated_list_1)
    print(f"After update 1, max: {ml.get_max()}")
    updated_list_2 = [4, 9, 1, 7, 2]
    ml.set_list(updated_list_2)
    print(f"After update 2, max: {ml.get_max()}")
    empty_list = []
    ml.set_list(empty_list)
    print(f"After update to empty list, max: {ml.get_max()}")