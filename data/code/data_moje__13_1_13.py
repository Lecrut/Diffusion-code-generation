def get_2d_element(matrix, row_index, col_index, fallback=None):
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
    result1 = get_2d_element(sample_matrix, 1, 1, "N/A")
    print(result1)
    result2 = get_2d_element(sample_matrix, 5, 5, "N/A")
    print(result2)
    result3 = get_2d_element(sample_matrix, 0, 2, "N/A")
    print(result3)
    result4 = get_2d_element([], 0, 0, "N/A")
    print(result4)
    result5 = get_2d_element([[1, 2], [3]], 1, 5, "N/A")
    print(result5)