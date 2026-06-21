def get_element_2d(matrix, row_index, col_index, default=None):
    if (
        matrix
        and 0 <= row_index < len(matrix)
        and 0 <= col_index < len(matrix[row_index])
    ):
        return matrix[row_index][col_index]
    return default

if __name__ == '__main__':
    sample_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result1 = get_element_2d(sample_matrix, 1, 2, "not found")
    print(result1)
    result2 = get_element_2d(sample_matrix, 5, 5, "not found")
    print(result2)
    result3 = get_element_2d(sample_matrix, 0, 0, "not found")
    print(result3)
    result4 = get_element_2d([], 0, 0, "not found")
    print(result4)
    result5 = get_element_2d([[1]], 0, 1, "not found")
    print(result5)