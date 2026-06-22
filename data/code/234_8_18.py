CHECKERBOARD_CELL_SIZE = 2

def format_checkerboard(matrix):
    formatted_board = []
    for row in matrix:
        formatted_row = ""
        for cell in row:
            formatted_row += "X" if cell else "."
        formatted_board.append(formatted_row * CHECKERBOARD_CELL_SIZE)
    return "\n".join(formatted_board)

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(format_checkerboard(sample_matrix))