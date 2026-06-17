def print_grid(rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(r * 10 + c, end=' ')
        print()
if __name__ == '__main__':
    rows = 3
    cols = 4
    print_grid(rows, cols)