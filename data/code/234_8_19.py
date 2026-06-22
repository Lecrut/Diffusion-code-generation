def bool_matrix_to_checkerboard(matrix):
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Invalid boolean matrix")

    checkerboard = ""
    for row in matrix:
        for cell in row:
            checkerboard += "X" if cell else "."
        checkerboard += "\n"

    return checkerboard

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(bool_matrix_to_checkerboard(sample_matrix))