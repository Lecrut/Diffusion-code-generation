def bool_matrix_to_checkerboard(matrix):
    checkerboard = []
    for row in matrix:
        checker_row = ''
        for cell in row:
            if cell:
                checker_row += 'X'
            else:
                checker_row += '.'
        checkerboard.append(checker_row)
    return '\n'.join(checkerboard)

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(bool_matrix_to_checkerboard(sample_matrix))