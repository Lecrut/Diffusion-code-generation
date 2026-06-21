def fetch_2d_element(matrix, row_index, col_index, fallback=None):
    if not isinstance(matrix, list):
        return fallback
    if row_index < 0 or row_index >= len(matrix):
        return fallback
    row = matrix[row_index]
    if not isinstance(row, list):
        return fallback
    if col_index < 0 or col_index >= len(row):
        return fallback
    return row[col_index]

if __name__ == '__main__':
    sample_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(fetch_2d_element(sample_matrix, 1, 1))
    print(fetch_2d_element(sample_matrix, 0, 2))
    print(fetch_2d_element(sample_matrix, 5, 5, fallback="OUT_OF_BOUNDS"))
    print(fetch_2d_element(sample_matrix, -1, 0, fallback="NEGATIVE_INDEX"))
    print(fetch_2d_element([], 0, 0, fallback="EMPTY_MATRIX"))
    print(fetch_2d_element([[1, 2]], 0, 10, fallback="COL_OUT_OF_BOUNDS"))