def generate_checkerboard():
    size = 5
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append(' ' * 3)
            else:
                row.append('*' * 3)
        board.append(row)
    return board
if __name__ == '__main__':
    checkerboard = generate_checkerboard()
    for row in checkerboard:
        print("".join(row))