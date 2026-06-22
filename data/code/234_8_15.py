def convert_to_checkerboard(matrix):
    checkerboard = []
    for row in matrix:
        checker_row = ''.join('X' if cell else ' ' for cell in row)
        checkerboard.append(checker_row)
    return checkerboard

def format_checkerboard(checkerboard):
    formatted_board = '\n'.join(row.center(20) for row in checkerboard)
    return formatted_board

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    
    checkerboard = convert_to_checkerboard(sample_matrix)
    formatted_board = format_checkerboard(checkerboard)
    print(formatted_board)