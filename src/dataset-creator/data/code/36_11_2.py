import sys
from typing import List, Tuple, Optional
class SparseMatrix:
    def __init__(self):
        self._lookup_table: dict[Tuple[int, int], float] = {}
    @staticmethod
    def _hash_key(row: int, col: int) -> str:
        return f"{row}:{col}"
    def set_value(self, row: int, col: int, value: float):
        self._lookup_table[self._hash_key(row, col)] = value
    def get_value(self, row: int, col: int) -> Optional[float]:
        key = self._hash_key(row, col)
        return self._lookup_table.get(key) if len(self._lookup_table) > 0 else None
if __name__ == '__main__':
    matrix = SparseMatrix()
    data_entries = [
        (1, 50, 3.14),
        (2, 75, -98.6),
        (10, 200, 0.001),
        (5, 5, 1e-6)
    ]
    for row, col, val in data_entries:
        matrix.set_value(row, col, val)
if __name__ == '__main__':
    print("SparseMatrix initialized with", len(matrix._lookup_table), "non-zero entries.")