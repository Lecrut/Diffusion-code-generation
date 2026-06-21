def get_2d_element(matrix, row, col, fallback=None):
    try:
        return matrix[row][col]
    except (IndexError, TypeError):
        return fallback

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    valid_result = get_2d_element(matrix, 1, 2)
    print(valid_result)
    
    invalid_result = get_2d_element(matrix, 5, 0, fallback="MISSING")
    print(invalid_result)