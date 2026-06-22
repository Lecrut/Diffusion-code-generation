class ListReverser:

    def __init__(self, data):
        self._data = data

    def reverse(self):
        if not isinstance(self._data, list):
            raise ValueError('Data must be a list')
        length = len(self._data)
        for i in range(length // 2):
            self._data[i], self._data[length - i - 1] = (self._data[length - i - 1], self._data[i])

    def get_data(self):
        return self._data
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    reverser = ListReverser(sample_list)
    reverser.reverse()
    print(reverser.get_data())