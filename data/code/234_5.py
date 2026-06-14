def print_checkerboard(size=6):
    for i in range(size):
        row = ""
        for j in range(size):
            if (i + j) % 2 == 0:
                row += "  "
            else:
                row += " "
        print(row)
        if i < size - 1:
            print()
if __name__ == '__main__':
    print_checkerboard(6)