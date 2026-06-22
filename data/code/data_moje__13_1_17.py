def get_nested_element(matrix, row_idx, col_idx, default=None):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return default
    if 0 <= row_idx < len(matrix):
        row = matrix[row_idx]
        if 0 <= col_idx < len(row):
            return row[col_idx]
    return default

if __name__ == '__main__':
    sample_matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    result_1 = get_nested_element(sample_matrix, 1, 2, default="Not Found")
    result_2 = get_nested_element(sample_matrix, 5, 0, default="Out of Bounds")
    result_3 = get_nested_element(sample_matrix, 0, 1, default="Default Val")
    print(result_1)
    print(result_2)
    print(result_3)