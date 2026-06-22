class ListReverser:

    def __init__(self, data):
        self._data = data

    def reverse(self):
        start_index = 0
        end_index = len(self._data) - 1
        while start_index < end_index:
            self._data[start_index], self._data[end_index] = (self._data[end_index], self._data[start_index])
            start_index += 1
            end_index -= 1

    def get_data(self):
        return self._data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    print('Original list:', reverser.get_data())
    reverser.reverse()
    print('Reversed list:', reverser.get_data())