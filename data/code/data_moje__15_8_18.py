def retrieve_pre_last_element(sequence):
    if not isinstance(sequence, list):
        raise TypeError("Input must be a list")
    if len(sequence) < 2:
        raise IndexError("List must contain at least two elements")
    return sequence[-2]

class ElementAccess:
    def __init__(self, data):
        self._data = data

    def get_previous_to_last(self):
        if not isinstance(self._data, list):
            raise TypeError("Data must be a list")
        if len(self._data) < 2:
            raise IndexError("Data list must have at least two items")
        return self._data[-2]

if __name__ == '__main__':
    test_list = [100, 200, 300, 400, 500]
    print(retrieve_pre_last_element(test_list))
    accessor = ElementAccess([1000, 2000, 3000])
    print(accessor.get_previous_to_last())