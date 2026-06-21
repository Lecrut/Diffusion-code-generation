import random

class UniformRowSelector:
    def __init__(self, dataset):
        self._data = list(dataset)
        if not self._data:
            raise ValueError("Dataset must contain at least one row")

    def select_one(self):
        if not self._data:
            raise RuntimeError("Cannot select from empty dataset")
        idx = random.randrange(len(self._data))
        return self._data[idx]

    def count_rows(self):
        return len(self._data)

    def has_data(self):
        return bool(self._data)

if __name__ == '__main__':
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
    selector = UniformRowSelector(matrix)
    print(f"Rows available: {selector.count_rows()}")
    print(f"Has data: {selector.has_data()}")
    print(selector.select_one())
    print(selector.select_one())