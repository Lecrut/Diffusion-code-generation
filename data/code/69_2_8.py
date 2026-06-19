class IndexManipulator:
    def __init__(self, data):
        self._data = data

    def reverse(self):
        left, right = 0, len(self._data) - 1
        while left < right:
            self._data[left], self._data[right] = self._data[right], self._data[left]
            left += 1
            right -= 1
        return self._data

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    manipulator = IndexManipulator(sample_list)
    reversed_list = manipulator.reverse()
    print(reversed_list)