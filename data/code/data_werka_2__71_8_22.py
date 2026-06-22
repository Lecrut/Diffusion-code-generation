class MiddleRetriever:
    def __init__(self, data):
        self._data = list(data)
        self._count = len(self._data)
        self._mid_idx = self._count // 2

    def get_middle(self):
        if self._count == 0:
            raise ValueError("Cannot retrieve middle of empty list")
        return self._data[self._mid_idx]

    def add(self, item):
        self._data.append(item)
        self._count += 1
        self._mid_idx = self._count // 2

    def remove_last(self):
        if self._count == 0:
            raise ValueError("Cannot remove from empty list")
        self._data.pop()
        self._count -= 1
        self._mid_idx = self._count // 2

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    retriever = MiddleRetriever(sample_data)
    middle_val = retriever.get_middle()
    print(middle_val)
    retriever.add(6)
    new_middle = retriever.get_middle()
    print(new_middle)
    retriever.remove_last()
    final_middle = retriever.get_middle()
    print(final_middle)