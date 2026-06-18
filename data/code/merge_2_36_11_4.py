import numpy as np
def create_sparse_matrix(rows: int = 1000, cols: int = 2000) -> dict:
    data_indices_values = []
    num_nonzero_entries = rows * cols // 10
    np.random.seed(42)
    row_indices = np.random.randint(0, rows + 1, size=num_nonzero_entries)
    col_indices = np.random.randint(0, cols + 1, size=num_nonzero_entries)
    values = np.random.rand(num_nonzero_entries).astype(np.float32)
    return {
        'rows': rows,
        'cols': cols,
        '_data_indices_values': data_indices_values if not num_nonzero_entries else None,                                              
        '__array__': np.column_stack((row_indices, col_indices)),
        '__values__': values
    }
def get_sparse_matrix(rows: int = 1000, cols: int = 2000) -> dict:
    num_nonzero_entries = rows * cols // 5
    np.random.seed(42)
    row_indices = np.random.randint(rows, size=num_nonzero_entries) + 1
    col_indices = np.random.randint(cols, size=num_nonzero_entries) + 1
    values = np.random.rand(num_nonzero_entries).astype(np.float32)
    return {
        'rows': rows,
        'cols': cols,
        '_data_indices_values': None,                                               
        '__array__': np.column_stack((row_indices, col_indices)),
        '__values__': values
    }
if __name__ == '__main__':
    sparse_data = get_sparse_matrix(rows=1024, cols=512)