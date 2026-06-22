def get_element_at_index(matrix, row, col, fallback):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return matrix[row][col]
    return fallback

if __name__ == '__main__':
    sample_data = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    print(get_element_at_index(sample_data, 1, 2, -1))
    print(get_element_at_index(sample_data, 5, 0, -1))
    print(get_element_at_index(sample_data, 0, 5, "N/A"))