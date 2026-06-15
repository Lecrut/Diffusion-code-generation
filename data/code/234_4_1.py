def create_checkerboard(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        board.append(row)
    return board
if __name__ == '__main__':
    n1 = 3
    result1 = create_checkerboard(n1)
    print(f"n={n1}:\n{result1}")
    n2 = 4
    result2 = create_checkerboard(n2)
    print(f"n={n2}:\n{result2}")
    n3 = 1
    result3 = create_checkerboard(n3)
    print(f"n={n3}:\n{result3}")