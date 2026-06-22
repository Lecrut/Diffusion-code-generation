def get_element_2d(matrix, row_index, col_index, fallback=None):
    try:
        row = matrix[row_index]
        return row[col_index]
    except (IndexError, TypeError):
        return fallback

if __name__ == '__main__':
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    result_valid = get_element_2d(data, 1, 2)
    print(result_valid)
    
    result_invalid = get_element_2d(data, 5, 0)
    print(result_invalid)