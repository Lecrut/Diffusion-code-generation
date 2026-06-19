class ListElementRetriever:
    MAX_INDEX = 1000
    MIN_INDEX = -1000

    def __init__(self, data):
        self._data = list(data)

    @staticmethod
    def is_valid_index(index, length):
        return ListElementRetriever.MIN_INDEX <= index < length and index <= ListElementRetriever.MAX_INDEX

    def get(self, index):
        if not self.is_valid_index(index, len(self._data)):
            raise IndexError("Index out of bounds")
        return self._data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ListElementRetriever(sample_list)
    print(f"Element at index 0: {retriever.get(0)}")
    print(f"Element at index 2: {retriever.get(2)}")
    print(f"Element at index -1: {retriever.get(-1)}")
    try:
        print(f"Element at index 5: {retriever.get(5)}")
    except IndexError as e:
        print(e)
    try:
        print(f"Element at index -6: {retriever.get(-6)}")
    except IndexError as e:
        print(e)