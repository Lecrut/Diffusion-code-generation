class DataReverser:
    def __init__(self, data):
        self._data = list(data)
    def reverse_data(self):
        self._data.reverse()
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = DataReverser(sample_list)
    print("Original list before reversal:", sample_list)
    reverser.reverse_data()
    print("List after reversal:", sample_list)