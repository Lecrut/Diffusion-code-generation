def print_checkerboard(size):
    for i in range(size):
        row = ""
        for j in range(size):
            if (i + j) % 2 == 0:
                row += " "
            else:
                row += "#"
        print(row)
if __name__ == '__main__':
    board_size = 5
    print_checkerboard(board_size)