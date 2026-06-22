def bool_matrix_to_checkerboard(matrix):
    checkerboard = []
    for row in matrix:
        checker_row = ''.join('X' if cell else 'O' for cell in row)
        checkerboard.append(checker_row)
    return '\n'.join(checkerboard)

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(bool_matrix_to_checkerboard(sample_matrix))