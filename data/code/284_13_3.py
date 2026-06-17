class DataReverser:
    def __init__(self, data):
        self._data = list(data)
    def reverse_internal_list(self):
        self._data.reverse()
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    reverser = DataReverser(sample_data)
    print("Original data:", sample_data)
    reverser.reverse_internal_list()
    print("Reversed data:", reverser._data)