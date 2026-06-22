class SafeListHandler:
    DEFAULT_VALUE = None

    def __init__(self, data):
        self._data = data

    @staticmethod
    def _is_valid_index(index, length):
        return 0 <= index < length

    def get_element(self, index):
        if self._is_valid_index(index, len(self._data)):
            return self._data[index]
        return SafeListHandler.DEFAULT_VALUE

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    handler = SafeListHandler(sample_list)
    print(handler.get_element(3))
    print(handler.get_element(0))
    print(handler.get_element(5))
    print(handler.get_element(-1))