if __name__ == '__main__':
    size = 5
    checkerboard = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append(" " * 3)
            else:
                row.append("X")
        checkerboard.append(row)
    for row in checkerboard:
        print(" ".join(row))