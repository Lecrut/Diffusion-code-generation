class ListElementRetriever:
    MAX_INDEX = 1000
    MIN_INDEX = -1000

    @staticmethod
    def validate_index(index):
        if index < ListElementRetriever.MIN_INDEX or index > ListElementRetriever.MAX_INDEX:
            raise IndexError('Index out of bounds')

    def __init__(self, data):
        self._data = list(data)

    def get(self, index):
        ListElementRetriever.validate_index(index)
        if 0 <= index < len(self._data) or -len(self._data) <= index < 0:
            return self._data[index]
        raise IndexError('Index out of bounds')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ListElementRetriever(sample_list)
    print(retriever.get(0))
    print(retriever.get(2))
    print(retriever.get(-1))
    try:
        retriever.get(5)
    except IndexError as e:
        print(e)
    try:
        retriever.get(-6)
    except IndexError as e:
        print(e)