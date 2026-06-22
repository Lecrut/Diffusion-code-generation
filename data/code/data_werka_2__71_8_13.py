class MiddleRetriever:
    def __init__(self, data):
        self._data = list(data)
        self._count = len(self._data)
        self._mid_idx = self._count // 2

    def _validate_non_empty(self):
        if self._count == 0:
            raise ValueError("Cannot retrieve middle of empty list")

    def get_middle(self):
        self._validate_non_empty()
        return self._data[self._mid_idx]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    retriever = MiddleRetriever(sample_data)
    print(retriever.get_middle())