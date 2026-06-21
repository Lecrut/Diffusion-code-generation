def fetch_2d_element(matrix, row_index, col_index, fallback):
    if not isinstance(matrix, list):
        return fallback
    if 0 <= row_index < len(matrix):
        row = matrix[row_index]
        if isinstance(row, list) and 0 <= col_index < len(row):
            return row[col_index]
    return fallback

if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = fetch_2d_element(data, 1, 2, -1)
    result2 = fetch_2d_element(data, 5, 0, "missing")
    result3 = fetch_2d_element(data, 1, 1, None)
    print(result1)
    print(result2)
    print(result3)