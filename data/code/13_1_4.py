def get_element_2d(data, row_index, col_index, default=None):
    try:
        return data[row_index][col_index]
    except IndexError:
        return default

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    valid_row = 1
    valid_col = 2
    valid_result = get_element_2d(matrix, valid_row, valid_col)
    print(valid_result)
    
    invalid_row = 5
    invalid_col = 0
    fallback = -1
    invalid_result = get_element_2d(matrix, invalid_row, invalid_col, default=fallback)
    print(invalid_result)