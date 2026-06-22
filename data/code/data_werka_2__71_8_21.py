class MiddleRetriever:
    def __init__(self, data):
        self._data = list(data)
        self._size = len(self._data)
        self._mid_idx = self._size // 2
        self._cached_mid = self._data[self._mid_idx] if self._size > 0 else None

    def get_middle(self):
        if self._size == 0:
            raise ValueError("List is empty")
        return self._cached_mid

    def add(self, value):
        self._data.append(value)
        self._size += 1
        new_idx = self._size // 2
        if new_idx != self._mid_idx:
            self._mid_idx = new_idx
            self._cached_mid = self._data[new_idx]

    def remove_last(self):
        if self._size == 0:
            raise ValueError("List is empty")
        self._data.pop()
        self._size -= 1
        new_idx = self._size // 2
        if new_idx != self._mid_idx:
            self._mid_idx = new_idx
            self._cached_mid = self._data[new_idx] if self._size > 0 else None

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50, 60, 70]
    retriever = MiddleRetriever(sample_values)
    middle_val = retriever.get_middle()
    print(middle_val)
    retriever.add(80)
    new_middle = retriever.get_middle()
    print(new_middle)
    retriever.remove_last()
    final_middle = retriever.get_middle()
    print(final_middle)