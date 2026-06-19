class ListReverser:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        self._data = data

    def reverse(self):
        left = 0
        right = len(self._data) - 1
        while left < right:
            self._data[left], self._data[right] = self._data[right], self._data[left]
            left += 1
            right -= 1
        return self._data

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    print(reverser.reverse())