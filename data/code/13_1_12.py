def get_element(matrix, row_idx, col_idx, fallback=None):
    try:
        row = matrix[row_idx]
        return row[col_idx]
    except (IndexError, TypeError):
        return fallback

if __name__ == '__main__':
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = get_element(data, 1, 2)
    print(result)
    result_fallback = get_element(data, 5, 0)
    print(result_fallback)