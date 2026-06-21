class SubListRetriever:

    def __init__(self, data):
        self._data = list(data)

    def get_sublist(self, start_index, end_index):
        if not (isinstance(start_index, int) and isinstance(end_index, int)):
            raise TypeError('Indices must be integers')
        if start_index < 0 or end_index >= len(self._data) or start_index > end_index:
            raise IndexError('Invalid index range')
        return self._data[start_index:end_index + 1]
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    retriever = SubListRetriever(sample_list)
    print(retriever.get_sublist(0, 2))
    print(retriever.get_sublist(1, 3))
    try:
        print(retriever.get_sublist(4, 6))
    except IndexError as e:
        print(e)