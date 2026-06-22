def print_asterisk_grid(size):
    for i in range(size):
        row = ''.join('*' if j % 2 == 0 else ' ' for j in range(size))
        print(row)

if __name__ == '__main__':
    grid_size = 15
    print_asterisk_grid(grid_size)