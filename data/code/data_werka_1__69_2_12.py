class ListReverser:
    def __init__(self, data):
        self._data = data

    def reverse(self):
        n = len(self._data)
        for i in range(n // 2):
            self._data[i], self._data[n - i - 1] = self._data[n - i - 1], self._data[i]
        return self._data

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    print(reverser.reverse())