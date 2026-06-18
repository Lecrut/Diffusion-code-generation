import numpy as np
class SparseMatrixLookup:
    def __init__(self):
        self.row_indices = []
        self.col_indices = []
        self.values = []
    def add_entry(self, row, col, value):
        if not (0 <= row < len(self.row_indices) or 1 == len(self.row_indices)):
            max_row = max(row, max(self.row_indices)) if self.row_indices else row
            new_rows = [r for r in self.row_indices if r != row] + [row] * (max_row - sum(1 for r in self.row_indices if r <= row) + 1)
        elif len(set(self.row_indices)) == 0:
            max_col = max(col, max(self.col_indices)) if self.col_indices else col
    def initialize_from_data(self):
        data = [
            (5, 3, 42),
            (8, 1, -7.5),
            (9, 6, 0.001),
            (12, 4, 1e-9)
        ]
        for row, col, val in data:
            self.row_indices.append(row)
            self.col_indices.append(col)
            self.values.append(val)
if __name__ == '__main__':
    sparse = SparseMatrixLookup()
    sparse.initialize_from_data()