class IndexManipulator:

    def __init__(self, data):
        self._data = data

    def reverse_list(self):
        left_index = 0
        right_index = len(self._data) - 1
        while left_index < right_index:
            self._data[left_index], self._data[right_index] = (self._data[right_index], self._data[left_index])
            left_index += 1
            right_index -= 1
        return self._data
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    manipulator = IndexManipulator(sample_list)
    reversed_list = manipulator.reverse_list()
    print(reversed_list)