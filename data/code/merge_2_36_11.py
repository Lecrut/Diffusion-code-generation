import sys
from collections import defaultdict
class SparseMatrix:
    def __init__(self):
        self._data = {}                                                             
    def set_value(self, row_idx, col_idx, val):
        if row_idx not in self._data:
            self._data[row_idx] = defaultdict(int)
        self._data[row_idx][col_idx] += val
    def get_value(self, row_idx, col_idx):
        return self._data.get(row_idx, {}).get(col_idx, 0.0)
    def size_nonzero(self):
        count = sum(len(cols) for cols in self._data.values())
        return count
if __name__ == '__main__':
    matrix = SparseMatrix()
    samples = [
        (0, 5, 1.2), (0, 8, -3.4),
        (1, 2, 7.89), (1, 15, 0.5),
        (3, 3, 100.0),
    ]
    for r, c, v in samples:
        matrix.set_value(r, c, v)
if __name__ == '__main__':
    print(f"Non-zero entries count: {matrix.size_nonzero()}")