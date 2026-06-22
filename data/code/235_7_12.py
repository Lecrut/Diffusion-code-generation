def generate_checkerboard(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    board = []
    for i in range(size):
        row = ['X' if (i + j) % 2 == 0 else '.' for j in range(size)]
        board.append(row)
    return board

def print_checkerboard(board):
    for row in board:
        print(''.join(row))

if __name__ == '__main__':
    sample_size = 4
    checkerboard = generate_checkerboard(sample_size)
    print_checkerboard(checkerboard)