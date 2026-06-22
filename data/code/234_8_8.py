def bool_matrix_to_checkerboard(matrix):
    checkerboard = []
    for row in matrix:
        line = ''
        for cell in row:
            if cell:
                line += 'X '
            else:
                line += '. '
        checkerboard.append(line.strip())
    return '\n'.join(checkerboard)

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(bool_matrix_to_checkerboard(sample_matrix))