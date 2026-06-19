class ListReverser:

    def __init__(self, data):
        self._data = data

    def reverse(self):
        if not isinstance(self._data, list):
            raise ValueError('Input must be a list')
        left_index = 0
        right_index = len(self._data) - 1
        while left_index < right_index:
            self._data[left_index], self._data[right_index] = (self._data[right_index], self._data[left_index])
            left_index += 1
            right_index -= 1
        return self._data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    print(reverser.reverse())