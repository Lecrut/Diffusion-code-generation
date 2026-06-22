def generate_checkerboard(matrix):
    if not all(isinstance(row, list) and len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Input must be a square boolean matrix.")
    
    checkerboard = []
    for i, row in enumerate(matrix):
        row_str = ""
        for j, cell in enumerate(row):
            if cell:
                row_str += 'X'
            else:
                row_str += ' '
        checkerboard.append(row_str)
    
    return "\n".join(checkerboard)

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(generate_checkerboard(sample_matrix))