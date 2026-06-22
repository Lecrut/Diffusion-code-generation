class ListElementRetriever:
    def __init__(self, data):
        self._data = data

    def _validate_index(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of bounds")

    def get_second(self):
        second_index = 1
        self._validate_index(second_index)
        return self._data[second_index]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    retriever = ListElementRetriever(my_list)
    second_element = retriever.get_second()
    print(second_element)