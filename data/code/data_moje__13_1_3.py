def fetch_2d_element(matrix, row, col, fallback):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return matrix[row][col]
    return fallback

if __name__ == '__main__':
    sample_matrix = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]
    print(fetch_2d_element(sample_matrix, 1, 1, -1))
    print(fetch_2d_element(sample_matrix, 0, 5, -1))
    print(fetch_2d_element(sample_matrix, 5, 0, -1))