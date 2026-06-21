def fetch_2d_element(matrix, row_idx, col_idx, fallback=None):
    try:
        return matrix[row_idx][col_idx]
    except (IndexError, TypeError):
        return fallback

if __name__ == '__main__':
    sample_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = fetch_2d_element(sample_matrix, 1, 2)
    print(result)
    result_out = fetch_2d_element(sample_matrix, 5, 0)
    print(result_out)
    result_none = fetch_2d_element([], 0, 0)
    print(result_none)