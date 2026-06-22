def get_2d_element(data, row_idx, col_idx, fallback):
    if row_idx < 0 or row_idx >= len(data):
        return fallback
    row = data[row_idx]
    if col_idx < 0 or col_idx >= len(row):
        return fallback
    return row[col_idx]

if __name__ == '__main__':
    sample_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = get_2d_element(sample_data, 1, 2, "NOT_FOUND")
    print(result1)
    result2 = get_2d_element(sample_data, 5, 0, "NOT_FOUND")
    print(result2)
    result3 = get_2d_element(sample_data, 0, 10, "NOT_FOUND")
    print(result3)
    result4 = get_2d_element(sample_data, 0, 0, "NOT_FOUND")
    print(result4)