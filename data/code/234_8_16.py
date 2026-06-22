def generate_checkerboard(rows, cols):
    board = []
    for r in range(rows):
        row_data = []
        for c in range(cols):
            if (r + c) % 2 == 0:
                row_data.append(' ')
            else:
                row_data.append('#')
        board.append(row_data)
    return board

def format_checkerboard(board):
    return '\n'.join([''.join(row) for row in board])

if __name__ == '__main__':
    sample_board = generate_checkerboard(5, 5)
    formatted_board = format_checkerboard(sample_board)
    print(formatted_board)