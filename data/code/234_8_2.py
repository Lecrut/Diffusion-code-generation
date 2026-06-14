if __name__ == '__main__':
    size = 5
    board = []
    for i in range(size):
        row = [i % 2 for j in range(size)]
        board.append(row)
    print(board)