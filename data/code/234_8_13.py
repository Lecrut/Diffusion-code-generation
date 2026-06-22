def is_valid_matrix(matrix):
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return False
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    if not all(len(row) == cols for row in matrix):
        return False
    return True

def matrix_to_checkerboard(matrix):
    if not is_valid_matrix(matrix):
        raise ValueError("Input must be a valid boolean matrix")
    
    checkerboard = []
    for r, row in enumerate(matrix):
        row_str = ""
        for c, cell in enumerate(row):
            if (r + c) % 2 == 0:
                row_str += " " if not cell else "#"
            else:
                row_str += "#" if not cell else " "
        checkerboard.append(row_str)
    return checkerboard

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(matrix_to_checkerboard(sample_matrix))