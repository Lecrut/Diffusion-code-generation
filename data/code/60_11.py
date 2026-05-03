class ArrayUtils:
    def __init__(self, data):
        self._data = data
    def retrieve_last(self):
        if not self._data:
            raise IndexError("Cannot retrieve last element from an empty list")
        return self._data[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    utils = ArrayUtils(sample_list)
    last_element = utils.retrieve_last()
    print(last_element)