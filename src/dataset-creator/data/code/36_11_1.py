import numpy as np
def create_sparse_matrix(rows: int = 1000, cols: int = 2000) -> dict:
    data = {}
    num_non_zeros = rows * cols // 10
    while len(data) < num_non_zeros:
        row_idx, col_idx = np.random.randint(0, rows), np.random.randint(0, cols)
        value = np.random.uniform(-5.0, 5.0)
        key = (row_idx, col_idx)
        if key not in data:
            data[key] = float(value)
    return {
        "rows": rows,
        "cols": cols,
        "_data": data
    }
if __name__ == '__main__':
    matrix_data = create_sparse_matrix(rows=500, cols=1000)
    sample_keys = list(matrix_data["_data"].keys())[:3]
    print(f"Matrix dimensions: {matrix_data['rows']}x{matrix_data['cols']}")
    print(f"Total non-zero entries stored: {len(matrix_data['_data'])}")
    for key in sample_keys:
        val = matrix_data["_data"][key]
        assert isinstance(val, float), "Value must be a float."
    test_key = (250, 750)
    if test_key in matrix_data["_data"]:
        print(f"Lookup result for {test_key}: {matrix_data['_data'][test_key]}")