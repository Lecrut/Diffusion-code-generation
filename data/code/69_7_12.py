class SubListRetriever:
    DEFAULT_START_INDEX = 0
    DEFAULT_END_INDEX = -1

    def __init__(self, data):
        self._data = list(data)

    @staticmethod
    def validate_indices(start, end, length):
        if not 0 <= start < length or not start <= end < length:
            raise IndexError('Start and end indices are out of bounds')

    def get_sublist(self, start=DEFAULT_START_INDEX, end=DEFAULT_END_INDEX):
        length = len(self._data)
        self.validate_indices(start, end, length)
        return self._data[start:end + 1]
if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55]
    retriever = SubListRetriever(sample_data)
    print(retriever.get_sublist(1, 3))
    print(retriever.get_sublist(0, 2))
    print(retriever.get_sublist(4, 5))