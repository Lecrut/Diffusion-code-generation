class MiddleRetriever:
    def __init__(self, data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Data must be a list or tuple")
        self._data = list(data)
        self._size = len(self._data)
        if self._size == 0:
            self._middle_val = None
        else:
            mid_idx = self._size // 2
            if self._size % 2 == 0:
                mid_idx -= 1
            self._middle_val = self._data[mid_idx]

    def get_middle(self):
        if self._size == 0:
            raise ValueError("Cannot retrieve middle of empty collection")
        return self._middle_val

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500, 600, 700]
    retriever = MiddleRetriever(sample_data)
    middle_val = retriever.get_middle()
    print(middle_val)