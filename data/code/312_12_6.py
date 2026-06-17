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
    def update_element(self, index, value):
        if 0 <= index < len(self._data):
            self._data[index] = value
            if value > self._max_element:
                self._max_element = value
            elif self._max_element is None and value > self._data[index]:
                 self._max_element = value
        else:
            raise IndexError("Index out of bounds")
    def get_max(self):
        return self._max_element
if __name__ == '__main__':
    initial_list = [10, 5, 20, 8]
    ml = MaxList(initial_list)
    print(f"Initial max: {ml.get_max()}")
    new_list_1 = [3, 7, 1, 9]
    ml.set_list(new_list_1)
    print(f"After set_list to {new_list_1}, max is: {ml.get_max()}")
    print("-" * 20)
    ml.update_element(1, 15)
    print(f"After update index 1 to 15, max is: {ml.get_max()}")
    ml.update_element(3, 25)
    print(f"After update index 3 to 25, max is: {ml.get_max()}")
    ml.update_element(0, 2)
    print(f"After update index 0 to 2, max is: {ml.get_max()}")