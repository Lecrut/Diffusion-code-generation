def fetch_2d_element(data, row_idx, col_idx, fallback):
    if 0 <= row_idx < len(data):
        row = data[row_idx]
        if 0 <= col_idx < len(row):
            return row[col_idx]
    return fallback

if __name__ == '__main__':
    grid = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    result_valid = fetch_2d_element(grid, 1, 2, "NOT_FOUND")
    print(result_valid)
    result_oob_row = fetch_2d_element(grid, 5, 0, "ROW_ERROR")
    print(result_oob_row)
    result_oob_col = fetch_2d_element(grid, 1, 5, "COL_ERROR")
    print(result_oob_col)
    result_short_row = fetch_2d_element([[1, 2], [3]], 1, 5, "DEFAULT")
    print(result_short_row)