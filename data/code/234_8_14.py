def bool_matrix_to_checkerboard(matrix):
    checkerboard = []
    for row in matrix:
        checkerboard_row = []
        for cell in row:
            if cell:
                checkerboard_row.append('X')
            else:
                checkerboard_row.append('.')
        checkerboard.append(checkerboard_row)
    return '\n'.join([' '.join(row) for row in checkerboard])

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(bool_matrix_to_checkerboard(sample_matrix))