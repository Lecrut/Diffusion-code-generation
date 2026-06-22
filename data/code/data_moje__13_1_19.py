def get_2d_element(matrix, row_index, col_index, fallback=None):
    if not isinstance(matrix, (list, tuple)):
        return fallback
    if row_index < 0 or row_index >= len(matrix):
        return fallback
    row = matrix[row_index]
    if not isinstance(row, (list, tuple)):
        return fallback
    if col_index < 0 or col_index >= len(row):
        return fallback
    return row[col_index]

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = get_2d_element(matrix, 1, 2)
    print(result1)
    result2 = get_2d_element(matrix, 3, 3)
    print(result2)
    result3 = get_2d_element(matrix, 0, 0, fallback="default")
    print(result3)
    result4 = get_2d_element(matrix, -1, 0)
    print(result4)
    result5 = get_2d_element([], 0, 0, fallback=42)
    print(result5)
    result6 = get_2d_element([[1]], 0, 5, fallback="out")
    print(result6)
    result7 = get_2d_element("not a list", 0, 0)
    print(result7)
    result8 = get_2d_element([[1, 2], "not a list"], 1, 0)
    print(result8)