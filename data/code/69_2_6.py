class IndexReverser:

    def __init__(self, data):
        self._data = data

    def reverse(self):
        length = len(self._data)
        for i in range(length // 2):
            self._data[i], self._data[length - i - 1] = (self._data[length - i - 1], self._data[i])
        return self._data
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    reverser = IndexReverser(sample_list)
    reversed_list = reverser.reverse()
    print(reversed_list)