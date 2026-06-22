def get_element_2d(matrix, row_index, col_index, fallback=None):
    try:
        if -len(matrix) <= row_index < len(matrix):
            row = matrix[row_index]
            if -len(row) <= col_index < len(row):
                return row[col_index]
        return fallback
    except Exception:
        return fallback

if __name__ == '__main__':
    sample_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = get_element_2d(sample_matrix, 1, 1)
    print(result1)
    result2 = get_element_2d(sample_matrix, 5, 5, 'OUT_OF_BOUNDS')
    print(result2)
    result3 = get_element_2d(sample_matrix, 0, 2)
    print(result3)
    result4 = get_element_2d([], 0, 0, 'EMPTY')
    print(result4)
    result5 = get_element_2d([[]], 0, 0, 'EMPTY_ROW')
    print(result5)